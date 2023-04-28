from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    disabled: Optional[bool] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    phone_number: Optional[str] = None

    class Config:
        orm_mode = True


class UserInDBSchema(UserSchema):
    hashed_password: str


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    phone_number: Optional[str] = None

    @validator("confirm_password")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v
