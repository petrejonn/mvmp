from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator


class TimestampMixin:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)


class User(Model, TimestampMixin):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=32, unique=True)
    email = fields.CharField(max_length=254, unique=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    address = fields.CharField(max_length=255, null=True)
    city = fields.CharField(max_length=255, null=True)
    state = fields.CharField(max_length=255, null=True)
    zip_code = fields.CharField(max_length=255, null=True)
    phone_number = fields.CharField(max_length=255, null=True)
    hashed_password = fields.CharField(
        max_length=100, validators=[MinLengthValidator(8)]
    )
    is_active = fields.BooleanField(default=False)
    activation_token = fields.CharField(max_length=100, null=True)
    reset_password_token = fields.CharField(max_length=100, null=True)
    reset_password_expires = fields.DatetimeField(null=True)

    class Meta:
        table = "user"

    def __str__(self):
        return self.email

    class PydanticMeta:
        exclude = [
            "hashed_password",
            "activation_token",
            "reset_password_token",
            "reset_password_expires",
        ]
