from typing import Optional
from pydantic import EmailStr, BaseModel


class UserSchemaIn(BaseModel):
    user_email: EmailStr
    password: str


class UserSchema(BaseModel):
    id: int
    user_email: EmailStr
    is_superuser: bool = False

