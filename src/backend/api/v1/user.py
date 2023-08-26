from datetime import datetime, timezone

import jwt
from fastapi import APIRouter

from src.backend.auth.auth import verify_password, create_access_token
from src.backend.config import settings
from src.backend.db.methods.user import UserRepository
from src.backend.schemas import CreateUserSchema, LoginUserSchema

user_router = APIRouter(
    prefix='/api/v1/user',
    tags=['user']
)


@user_router.post('/create_user')
async def create_user(user: CreateUserSchema) -> dict:
    new_user = UserRepository().create_user(user)
    return {'user': new_user}


@user_router.post('/login_user')
async def get_user(user: LoginUserSchema) -> dict:
    login_user = user.model_dump()
    plain_password = login_user['hashed_password']
    hashed_password = UserRepository().get_password_by_username(login_user['username'])
    return verify_password(login_user['username'], plain_password, hashed_password)


@user_router.get('/verify_token/')
async def check_correct_token(username, access_token, refresh_token):
    try:
        jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
        return True
    except:
        try:
            jwt.decode(refresh_token, settings.SECRET_KEY, settings.ALGORITHM)
            return {'access': create_access_token(username)}
        except:
            return False


@user_router.post('/get_user/{user_id}')
async def get_user(user_id: int):
    user = UserRepository().get_user_by_id(user_id)
    return user
