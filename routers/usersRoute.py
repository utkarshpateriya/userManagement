from fastapi import APIRouter, Depends
from schemas import userSchema
from database import SessionLocal
from sqlalchemy.orm import Session
from utils import userUtils

router = APIRouter(
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/signup')
def signup(user: userSchema.CreateUser, db: Session = Depends(get_db)):
    pass