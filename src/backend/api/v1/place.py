from fastapi import APIRouter

from src.backend.schemas import CreatePlaceSchema

place_router = APIRouter(
    prefix='/api/v1/place',
    tags=['place']
)


@place_router.post('/create_place')
async def create_place(
        place: CreatePlaceSchema
):
    return ...


@place_router.post('/add_folder_place_associations')
async def add_folder_place_associations():
    return ...


@place_router.post('/get_places_by_tags')
async def get_places_by_tags():
    return ...
