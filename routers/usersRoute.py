from fastapi import APIRouter, Depends
from schemas import userSchema
from database import SessionLocal
from sqlalchemy.orm import Session
from utils.userUtils import UserUtils

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
    user_utils = UserUtils()
    return user_utils.create_user(user=user, db=db)

@router.post('/login')
def login(user: userSchema.CreateUser, db: Session = Depends(get_db)):
    user_utils = UserUtils()
    return user_utils.login_user(user=user, db=db)