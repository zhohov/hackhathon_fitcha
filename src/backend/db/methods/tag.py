from src.backend.db.database import session
from src.backend.models.models import Tag


class TagRepository:
    model = Tag

    def create_tag(self, data):
        tag = self.model(**data.model_dump())
        session.add(tag)
        session.commit()
        return tag.id

    def get_all_tags(self):
        tags = session.query(self.model).all()
        return tags

    def get_tag_by_id(self, tag_id: int):
        tag = session.query(self.model).filter(self.model.id == tag_id).first()
        return tag

