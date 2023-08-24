from fastapi import APIRouter

from src.backend.schemas import CreateFolderSchema

folder_router = APIRouter(
    prefix='/api/v1/folder',
    tags=['folder']
)


@folder_router.post('/create_folder')
async def create_folder(
        folder: CreateFolderSchema
):
    return ...


@folder_router.post('/get_folders_by_user_id')
async def get_folders_by_user_id():
    return ...


@folder_router.post('/get_folder_and_places_by_user_id')
async def get_folder_and_places_by_user_id():
    return ...
