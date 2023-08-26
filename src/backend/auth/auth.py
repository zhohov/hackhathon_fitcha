from datetime import datetime, timezone, timedelta

import jwt

from fastapi import HTTPException
from passlib.context import CryptContext
from starlette import status

from src.backend.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
secret_key = settings.SECRET_KEY
algorithms = settings.ALGORITHM


def get_hashed_password(password: str) -> pwd_context.hash:
    return pwd_context.hash(password)


def verify_password(username: str, plain_password: str, hashed_password: str):
    if not pwd_context.verify(plain_password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )

    else:
        return {
            'access': create_access_token(username),
            'refresh': create_refresh_token(username)
        }


def create_access_token(username: str) -> jwt:
    expires_delta = datetime.now(timezone.utc) + timedelta(minutes=5)
    to_encode = {"exp": expires_delta, "sub": username}
    access_token = jwt.encode(to_encode, secret_key, algorithm=algorithms)
    return access_token

def create_refresh_token(username: str) -> jwt:
    expires_delta = datetime.now(timezone.utc) + timedelta(hours=150)
    to_encode = {"exp": expires_delta, "sub": username}
    access_token = jwt.encode(to_encode, secret_key, algorithms)
    return access_token

