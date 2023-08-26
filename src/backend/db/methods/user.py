from src.backend.auth.auth import get_hashed_password
from src.backend.db.database import session
from src.backend.models.models import User


class UserRepository:
    model = User

    def create_user(self, data) -> int:
        user = self.model(**data.model_dump())
        user.hashed_password = get_hashed_password(user.hashed_password)
        session.add(user)
        session.commit()
        return user.id

    def get_user_by_id(self, user_id: int):
        user = session.query(self.model).filter(self.model.id == user_id).first()
        return user.folders

    def get_password_by_username(self, username: str):
        user = session.query(self.model).filter(self.model.username == username).first()
        return user.hashed_password

    def get_user_with_folders(self, user_id: int):
        user = session.query(self.model).filter(self.model.id == user_id).first()
        folders = user.folders
        user_with_folders = {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "hashed_password": user.hashed_password
            },
            "folders": [{
                "id": folder.id,
                "name": folder.name,
                "desc": folder.desc
            } for folder in folders]
        }
        return user_with_folders
