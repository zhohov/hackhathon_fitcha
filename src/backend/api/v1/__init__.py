__all__ = ['root_router', 'user_router', 'folder_router', 'place_router', 'tag_router', 'city_router']

from src.backend.api.v1.city import city_router
from src.backend.api.v1.folder import folder_router
from src.backend.api.v1.place import place_router
from src.backend.api.v1.root import root_router
from src.backend.api.v1.tag import tag_router
from src.backend.api.v1.user import user_router

