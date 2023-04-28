from typing import Optional
from passlib.context import CryptContext
from pydantic import EmailStr

from app.user.models.user import User
from app.user.schemas.user_schema import UserCreateSchema
from app.user.services.security import create_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_by_username(username: str) -> Optional[User]:
    return await User.get_or_none(username=username)


async def get_user_by_email(email: EmailStr) -> Optional[User]:
    return await User.get_or_none(email=email)


async def create_user(user: UserCreateSchema) -> User:
    hashed_password = pwd_context.hash(user.password)
    activation_token = create_token()

    user_obj = await User.create(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        address=user.address,
        city=user.city,
        state=user.state,
        zip_code=user.zip_code,
        phone_number=user.phone_number,
        activation_token=activation_token,
    )
    return user_obj


async def send_email_verification(email: str, token: str):
    # Code to send email verification
    pass


# def generate_password_reset_token(user: User) -> str:
#     data = {"sub": user.username, "type": "password_reset"}
#     token = create_access_token(data)
#     user.reset_password_token = token
#     user.reset_password_expires = datetime.utcnow() + timedelta(hours=1)
#     user.save()
#     return token
