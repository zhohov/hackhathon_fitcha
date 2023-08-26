from src.backend.db.database import session
from src.backend.models.models import City


class CityRepository:
    model = City

    def create_tag(self, data):
        city = self.model(**data.model_dump())
        session.add(city)
        session.commit()
        return city.id

    def get_all_tags(self):
        city = session.query(self.model).all()
        return city
