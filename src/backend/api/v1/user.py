from fastapi import APIRouter

from src.backend.schemas import CreateUserSchema, LoginUserSchema

user_router = APIRouter(
    prefix='/api/v1/user',
    tags=['user']
)


@user_router.post('/create_user')
async def create_user(
        user: CreateUserSchema
):
    return ...


@user_router.post('/login_user')
async def get_user(
        user: LoginUserSchema
):
    return ...
