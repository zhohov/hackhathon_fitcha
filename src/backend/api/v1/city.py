from fastapi import APIRouter

from src.backend.db.methods.city import CityRepository
from src.backend.schemas.city import CreateCitySchema

city_router = APIRouter(
    prefix='/api/v1/city',
    tags=['city']
)


@city_router.post('/create_city')
async def create_tag(tag: CreateCitySchema):
    new_city = CityRepository().create_tag(tag)
    return new_city


@city_router.get('/get_cities')
async def get_tags():
    cities = CityRepository().get_all_tags()
    return cities
