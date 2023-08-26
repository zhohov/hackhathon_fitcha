from fastapi import APIRouter

from src.backend.db.methods.tag import TagRepository
from src.backend.schemas.tag import CreateTagSchema

tag_router = APIRouter(
    prefix='/api/v1/tag',
    tags=['tag']
)


@tag_router.post('/create_tag')
async def create_tag(tag: CreateTagSchema):
    new_tag = TagRepository().create_tag(tag)
    return new_tag


@tag_router.get('/get_tags')
async def get_tags():
    tags = TagRepository().get_all_tags()
    return tags


@tag_router.post('/get_tag_by_id/{tag_id}')
async def get_tags(tag_id: int):
    tag = TagRepository().get_tag_by_id(tag_id)
    return tag
