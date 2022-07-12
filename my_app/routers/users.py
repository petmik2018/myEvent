from typing import List
from fastapi import HTTPException
from fastapi import APIRouter, Depends, status

from my_app.crud.users import read_user, read_users, create_user
from my_app.schemas.users import UserSchema, UserSchemaIn
from my_app.security import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# @router.get("/", response_model=List[UserSchema])
# async def read_users(current_user: UserSchema = Depends(get_current_user)):
#     print("current_user: ", current_user)
#     users_list = await get_users_list()
#     return users_list

@router.get("/", response_model=List[UserSchema])
async def get_users():
    users_list = await read_users()
    return users_list


@router.get("/me", response_model=UserSchema)
async def get_user(current_user: UserSchema = Depends(get_current_user)):
    print("current_user: ", current_user)
    user = await read_user(current_user.user_id)
    return user


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSchema
)
async def insert_user(user: UserSchemaIn):
    new_user = await create_user(user)
    return new_user

