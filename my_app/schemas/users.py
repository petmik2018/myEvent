from typing import Optional
from pydantic import EmailStr, BaseModel


class UserSchemaIn(BaseModel):
    username: EmailStr
    password: str


class UserSchema(BaseModel):
    id: int
    username: EmailStr

