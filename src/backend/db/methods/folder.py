from typing import Optional

from src.backend.db.database import session
from src.backend.db.methods.user import UserRepository
from src.backend.models.models import Folder, User


class FolderRepository:
    model = Folder
    user_model = User

    def create_folder(self, data):
        folder = self.model(**data.model_dump())
        session.add(folder)
        session.commit()

        return folder

    def get_user_folders(self, user_id: int):
        user = session.query(self.user_model).filter(self.user_model.id == user_id).first()
        user_folders = user.folders
        folders = {
            "folders": [{
                "id": folder.id,
                "name": folder.name,
                "desc": folder.desc
            } for folder in user_folders]
        }
        return folders


