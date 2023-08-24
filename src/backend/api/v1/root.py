from fastapi import APIRouter

root_router = APIRouter(
    tags=['root']
)


@root_router.get('/')
async def root():
    return {'Hello': 'World'}
