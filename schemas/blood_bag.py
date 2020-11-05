from ma import ma
from models.blood_bag import BloodBag
from marshmallow import post_load


class BloodBagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BloodBag
        # load_only = ()
        dump_only = ("id", "bank_id")

    @post_load
    def make_blood_bag(self, data, **kwargs):
        return BloodBag(**data)

