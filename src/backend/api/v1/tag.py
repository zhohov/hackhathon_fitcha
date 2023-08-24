from fastapi import APIRouter

tag_router = APIRouter(
    prefix='/api/v1/tag',
    tags=['tag']
)


@tag_router.post('/create_tag')
async def create_user_request():
    return ...


@tag_router.get('/tags')
async def get_tags():
    return ...
