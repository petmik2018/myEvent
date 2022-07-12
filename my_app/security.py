from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from my_app.schemas.auth import TokenData


SECRET_KEY = "40702ffbf57ce4ae11a2cd825bb5761c674e36ba8c221d47eed455a0d1a93629"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
access_token_jwt_subject = "access"
superuser_username = "petmik@yandex.ru"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("payload: ", payload)
        user_id: str = payload.get("user_id")
        username: str = payload.get("username")
        if username is None:
            raise credential_exceptions
        token_data = TokenData(user_id=user_id, username=username)
        print("token_data: ", token_data)
    except JWTError:
        raise credential_exceptions
    return(token_data)


