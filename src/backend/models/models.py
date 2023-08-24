from sqlalchemy import Column, Table, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

Base = declarative_base()


folder_place_association = Table(
    'folder_place_association',
    Base.metadata,
    Column('folder_id', Integer, ForeignKey('folders.id')),
    Column('place_id', Integer, ForeignKey('places.id'))
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    hashed_password: Mapped[str] = mapped_column()


class Folder(Base):
    __tablename__ = 'folders'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column()
    desc: Mapped[str] = mapped_column()

    places: Mapped[list['Place']] = relationship(
        secondary=folder_place_association,
        back_populates='folders',
        lazy=True
    )


class Place(Base):
    __tablename__ = 'places'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column()
    desc: Mapped[str] = mapped_column()
    coord: Mapped[str] = mapped_column()

    tag: Mapped[int] = mapped_column(ForeignKey('places.id'))

    folders: Mapped[list['Folder']] = relationship(
        secondary=folder_place_association,
        back_populates='places',
        lazy=True
    )


class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    places: Mapped[list['Place']] = relationship()
