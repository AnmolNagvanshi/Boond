from flask import Flask, jsonify
from config import Config

from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from marshmallow import ValidationError

from db import db
from ma import ma

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@app.route('/')
def hello_world():
    return 'Hello World!'


db.init_app(app)
ma.init_app(app)

from models import user, blood_bag, blood_bank, bag_size


if __name__ == '__main__':
    app.run()

