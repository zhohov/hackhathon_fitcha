from fastapi import HTTPException

from src.backend.db.database import session
from src.backend.models.models import Place, Tag, Folder


class PlaceRepository:
    model = Place
    tag_model = Tag
    folder_model = Folder

    def create_place(self, data):
        place = self.model(**data.model_dump())
        session.add(place)
        session.commit()
        return place.id

    def get_places(self):
        places = session.query(self.model).all()
        return places

    def get_places_by_tag(self, tag_id: int):
        tags = session.query(self.tag_model).filter(self.tag_model.id == tag_id).first()
        places = tags.places
        tag_with_places = {
            "tag": {
                "id": tags.id,
                "name": tags.name,
            },
            "places": [{
                "id": place.id,
                "name": place.name,
                "desc": place.desc,
                "coord1": place.coord1,
                "coord2": place.coord2,
                "city": place.city
            } for place in places]
        }
        return tag_with_places

    def get_places_by_city(self, city_id: int):
        city = session.query(self.tag_model).filter(self.tag_model.id == city_id).first()
        places = city.places
        city_with_places = {
            "tag": {
                "id": city.id,
                "name": city.name,
            },
            "places": [{
                "id": place.id,
                "name": place.name,
                "desc": place.desc,
                "coord": place.coord
            } for place in places]
        }
        return city_with_places

    def add_folder_place_associations(self, data):
        data = data.model_dump()
        folder = session.query(self.folder_model).filter(self.folder_model.id == data['folder_id']).first()
        place = session.query(self.model).filter(self.model.id == data['folder_id']).first()

        if not folder or not place:
            raise HTTPException(status_code=404, detail="error")

        folder.places.append(place)
        session.commit()

        return {"message": "ok"}

    def get_places_in_folder(self, folder_id: id):
        folder = session.query(self.folder_model).filter(self.folder_model.id == folder_id).first()
        places = folder.places

        folder_and_places = {
            "folder": {
                "id": folder.id,
                "name": folder.name
            },
            "places": [{
                "id": place.id,
                "name": place.name
            } for place in places]
        }

        return folder_and_places

