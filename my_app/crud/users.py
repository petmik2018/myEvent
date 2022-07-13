from fastapi import HTTPException

from my_app.database import my_database
from my_app.tables import users_table
from my_app.schemas.users import UserSchemaIn
from my_app.security import superuser_username

from passlib.hash import pbkdf2_sha256


async def read_users():
    query = users_table.select()
    return await my_database.fetch_all(query=query)


async def read_user(user_id: int):
    query = users_table.select().where(users_table.c.id == user_id)
    return await my_database.fetch_one(query=query)


async def create_user(user: UserSchemaIn):
    hashed_password = pbkdf2_sha256.hash(user.password)
    is_me = (superuser_username == user.user_email)
    query = users_table.insert().values(
        user_email=user.user_email,
        hashed_password=hashed_password,
        is_superuser=is_me,
    )
    user_id = await my_database.execute(query)
    return {**user.dict(), "id": user_id}
