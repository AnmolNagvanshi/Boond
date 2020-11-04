from ma import ma
from models.blood_bank import BloodBank
from marshmallow import post_load


class BloodBankSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BloodBank
        load_only = ("password",)
        dump_only = ("id",)

    @post_load
    def make_blood_bank(self, data, **kwargs):
        return BloodBank(**data)

