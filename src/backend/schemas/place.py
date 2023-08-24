from pydantic import BaseModel


class CreatePlaceSchema(BaseModel):
    name: str
    desc: str
    coord: str
