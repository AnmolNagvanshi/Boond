from ma import ma
from models.donation import Donation
from marshmallow import post_load, fields


class DonationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Donation
        dump_only = ('id', 'user_id', )
        include_fk = True

    blood_bank_id = fields.Int(required=True)

    @post_load
    def make_donation(self, data, **kwargs):
        return Donation(**data)

