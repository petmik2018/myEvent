from typing import List
from fastapi import HTTPException
from fastapi import APIRouter, Depends, status

from my_app.database import my_database

from my_app.crud.users import read_users as get_users_list
from my_app.tables import users_table
from my_app.schemas.users import UserSchema, UserSchemaIn
from my_app.security import get_current_user


from passlib.hash import pbkdf2_sha256


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=List[UserSchema])
async def read_users(current_user: UserSchema = Depends(get_current_user)):
    print(current_user)
    users_list = await get_users_list()
    return users_list
# async def read_users():
#     users_list = await get_users_list()
#     return users_list


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSchema
)
async def insert_user(user: UserSchemaIn):
    hashed_password = pbkdf2_sha256.hash(user.password)
    query = users_table.insert().values(
        username=user.username,
        password=hashed_password
    )
    user_id = await my_database.execute(query)
    return {**user.dict(), "id": user_id}
