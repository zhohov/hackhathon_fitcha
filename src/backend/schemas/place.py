from typing import Optional

from pydantic import BaseModel


class CreatePlaceSchema(BaseModel):
    imgURL: Optional[str] = None
    name: str
    desc: str
    coord1: str
    coord2: str
    tag: int
    city: int


class AddFolderPlaceAssociation(BaseModel):
    folder_id: int
    place_id: int
