from sqlalchemy import Column, String, Integer

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), index=True)
    description = Column(String(500), index=True)