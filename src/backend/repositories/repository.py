from abc import ABC, abstractmethod


class InterfaceRepository(ABC):

    @abstractmethod
    def create_item():
        raise NotImplementedError

    @abstractmethod
    def get_items():
        raise NotImplementedError

    @abstractmethod
    def get_item_by_id():
        raise NotImplementedError


class SQLAlchemyRepository(InterfaceRepository):
    model = None

    def create_item(self):
        return ...

    def get_items(self):
        return ...

    def get_item_by_id(self):
        return ...
