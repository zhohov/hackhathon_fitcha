from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.backend.config import settings

engine = create_engine(settings.DB_URL, echo=True)
session = Session(engine)
