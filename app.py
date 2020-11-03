from flask import Flask, jsonify
from config import Config

from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError

from db import db
from ma import ma
from blacklist import BLACKLIST

from resources.auth import LoginAPI, LogoutAPI
from resources.user import UserListAPI, UserAPI

app = Flask(__name__)
app.config.from_object(Config)

# Flask extensions
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token) -> bool:
    return decrypted_token["jti"] in BLACKLIST


api.add_resource(LoginAPI, "/login")
api.add_resource(LogoutAPI, "/logout")

api.add_resource(UserListAPI, "/users")
api.add_resource(UserAPI, "/users/<int:user_id>")


@app.route('/')
def hello_world():
    return 'Hello World!'


db.init_app(app)
ma.init_app(app)

from models import user, blood_bag, blood_bank, bag_size

if __name__ == '__main__':
    app.run()
