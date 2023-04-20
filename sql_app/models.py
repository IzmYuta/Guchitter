from sqlalchemy import Column, Integer, String

from .database import Base


class Guchi(Base):
    __tablename__ = "guchi"
    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String)
