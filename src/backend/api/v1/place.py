from fastapi import APIRouter

from src.backend.db.methods.place import PlaceRepository
from src.backend.schemas import CreatePlaceSchema
from src.backend.schemas.place import AddFolderPlaceAssociation

place_router = APIRouter(
    prefix='/api/v1/place',
    tags=['place']
)


@place_router.post('/create_place')
async def create_place(
        place: CreatePlaceSchema
):
    new_place = PlaceRepository().create_place(place)
    return new_place


@place_router.get('/all_places')
async def get_all_places():
    return PlaceRepository().get_places()


@place_router.post('/add_folder_place_associations')
async def add_folder_place_associations(association: AddFolderPlaceAssociation):
    folder_place = PlaceRepository().add_folder_place_associations(association)
    return folder_place


@place_router.get('/get_places_by_tags/{tag_id}')
async def get_places_by_tags(tag_id: int):
    places = PlaceRepository().get_places_by_tag(tag_id)
    return places


@place_router.get('/get_places_by_city/{city_id}')
async def get_places_by_tags(city_id: int):
    places = PlaceRepository().get_places_by_city(city_id)
    return places


@place_router.get('/get_places_in_folder/{folder_id}')
def get_places_in_folder(folder_id: int):
    result = PlaceRepository().get_places_in_folder(folder_id)
    return result
