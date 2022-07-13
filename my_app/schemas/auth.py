from typing import Optional
from pydantic import EmailStr, BaseModel


class TokenData(BaseModel):
    user_id: Optional[int] = None
    user_email: Optional[EmailStr] = None

