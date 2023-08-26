from fastapi import APIRouter

from src.backend.db.methods.folder import FolderRepository
from src.backend.schemas import CreateFolderSchema

folder_router = APIRouter(
    prefix='/api/v1/folder',
    tags=['folder']
)


@folder_router.post('/create_folder')
async def create_folder(
        folder: CreateFolderSchema
):
    new_folder = FolderRepository().create_folder(folder)
    return new_folder


@folder_router.post('/get_folders_by_user_id/{user_id}')
async def get_folders_by_user_id(user_id: int):
    folders = FolderRepository().get_user_folders(user_id)
    return folders


@folder_router.post('/get_folder_and_places_by_user_id')
async def get_folder_and_places_by_user_id():
    return ...
