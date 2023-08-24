from typing import Optional

from pydantic import BaseModel


class CreateFolderSchema(BaseModel):
    name: str
    desc: Optional[str] = None
    user_id: int
