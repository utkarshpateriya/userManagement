from sqlalchemy import Column, Integer, String
from database import Base

class UserModal(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True)
    password = Column(String(100))