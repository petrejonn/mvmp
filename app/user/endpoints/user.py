from fastapi import APIRouter, Body, HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)
from tortoise.transactions import in_transaction

from app.user.schemas.user_schema import UserCreateSchema, UserSchema
from app.user.services.utils import (
    create_user,
    get_user_by_email,
    get_user_by_username,
    send_email_verification,
)


router = APIRouter()


@router.post("/register", response_model=UserSchema, status_code=HTTP_201_CREATED)
async def register_user(user: UserCreateSchema = Body(...)):
    existing_user = await get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail="Username already exists",
        )
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail="Email already exists",
        )
    async with in_transaction():
        user_obj = await create_user(user)

    await send_email_verification(user.email, user_obj.activation_token)
    return await UserSchema.from_orm(user_obj)


# @router.get("/verify-email", response_model=Dict[str, Any])
# def verify_email(token: str):
#     try:
#         payload = jwt.decode(token, User.SECRET_KEY, algorithms=[User.ALGORITHM])
#         username: str = payload.get("sub")
#         user = get_user_by_username(username)
#         if not user:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="User not found",
#             )
#         if user.activation_token != token:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Invalid token",
#             )
#         user.activation_token = None
#         user.is_active = True
#         user.save()
#         return {"message": "Email verified successfully"}
#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Invalid token",
#         )
