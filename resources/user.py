from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt,
)
from models.user import User
from schemas.user import UserSchema

# Error Messages
USER_ALREADY_EXISTS = "A user with that username already exists."
CREATED_SUCCESSFULLY = "User created successfully."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
INVALID_CREDENTIALS = "Invalid credentials!"
USER_LOGGED_OUT = "User <id={}> successfully logged out."

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)


class UserRegister(Resource):

    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)

        if User.find_by_username(user.username):
            return {"message": USER_ALREADY_EXISTS}, 400

        user.save_to_db()
        return {"message": CREATED_SUCCESSFULLY}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)

        user = User.find_by_username(user_data.username)

        if user and safe_str_cmp(user_data.password, user.password_hash):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": INVALID_CREDENTIALS}, 401


class UserResource(Resource):

    @classmethod
    @jwt_required
    def get(cls, user_id: int):
        user = User.find_by_id(user_id)
        if not user:
            return {"message": USER_NOT_FOUND}, 404

        return user_schema.dump(user), 200

    @classmethod
    @jwt_required
    def delete(cls, user_id: int):
        user = User.find_by_id(user_id)
        if not user:
            return {"message": USER_NOT_FOUND}, 404

        user.delete_from_db()
        return {"message": USER_DELETED}, 200


class UserList(Resource):

    @classmethod
    @jwt_required
    def get(cls):
        user_list = user_list_schema.dump(User.find_all())
        return {"items": user_list}, 200
