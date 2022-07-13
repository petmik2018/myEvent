from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from my_app.database import my_database

from my_app.tables import users_table
from my_app.security import create_access_token
from passlib.hash import pbkdf2_sha256


router = APIRouter(
    tags=["Auth"]
)


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    query = users_table.select().where(users_table.c.user_email == form.username)
    my_user = await my_database.fetch_one(query=query)

    if not my_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not pbkdf2_sha256.verify(form.password, my_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")

    access_token = create_access_token(
        data={"user_id": my_user.id}
    )
    return {"access_token": access_token, "token_type": "bearer"}

