from ma import ma
from models.user import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        load_only = ("password",)
        # dump_only = ("id",)

