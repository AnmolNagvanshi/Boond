from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from models.blood_bank import BloodBank
from schemas.blood_bank import BloodBankSchema

from utilities import geo
# from utilities.blood_group import BloodGroupType

# Response Messages
BANK_ALREADY_EXISTS = "A blood bank with that email already exists."
CREATED_SUCCESSFULLY = "Blood bank account created successfully."
BANK_NOT_FOUND = "Blood bank not found."
BANK_DELETED = "Blood bank account deleted."

bank_schema = BloodBankSchema()
bank_list_schema = BloodBankSchema(many=True)


class BankListAPI(Resource):

    @classmethod
    # @jwt_required
    def get(cls):
        req = request.args

        # Banks by state and city
        if 'state' in req and 'city' in req:
            banks = BloodBank.find_all_by_state_city(req['state'], req['city'])

        # Banks by distance
        elif 'lati' in req and 'longi' in req and 'radius' in req:
            all_banks = BloodBank.find_all()
            # filter and sort banks by distance
            banks = geo.sort_by_distance(all_banks, float(req['lati']), float(req['longi']), float(req['radius']))

        else:
            banks = BloodBank.find_all()

        bank_list = bank_list_schema.dump(banks)

        return {"banks": bank_list}, 200

    @classmethod
    def post(cls):
        bank_json = request.get_json()
        bank = bank_schema.load(bank_json)

        if BloodBank.find_by_email(bank.email):
            return {"message": BANK_ALREADY_EXISTS}, 400

        bank.save_to_db()
        return {"message": CREATED_SUCCESSFULLY}, 201


class BankAPI(Resource):

    @classmethod
    # @jwt_required
    def get(cls, bank_id: int):
        bank = BloodBank.find_by_id(bank_id)
        if not bank:
            return {"message": BANK_NOT_FOUND}, 404

        return bank_schema.dump(bank), 200

    @classmethod
    @jwt_required
    def delete(cls, bank_id: int):
        bank = BloodBank.find_by_id(bank_id)
        if not bank:
            return {"message": BANK_NOT_FOUND}, 404

        bank.delete_from_db()
        return {"message": BANK_DELETED}, 200


# class BanksByDistanceAPI(Resource):
#
#     @classmethod
#     def get(cls, lati: float, longi: float, radius: float):
#         banks = BloodBank.find_all()
#
#         # filter and sort banks by distance
#         sorted_banks = geo.sort_by_distance(banks, lati, longi, radius)
#
#         return {"banks": bank_list_schema.dump(sorted_banks)}, 200
#
#
# class BanksByStateAndCity(Resource):
#
#     @classmethod
#     def get(cls, state: str, city: str):
#         banks = BloodBank.find_all_by_state_city(state, city)
#
#         return {"banks": bank_list_schema.dump(banks)}, 200


# class BanksByQuantityOfBloodAPI(Resource):
#
#     @classmethod
#     def get(cls, group: int):
#         blood_group = BloodGroupType(group)
#         bags = BloodBag.find_all_by_bank_and_group()
#
