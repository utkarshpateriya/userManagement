from passlib.context import CryptContext
from schemas import userSchema
from sqlalchemy.orm import Session
from models.userModel import UserModal
from fastapi import HTTPException, status
from jose import jwt
from config import SECRET_KEY, ALGORITHM

import re

class UserUtils:
    pwd_context = CryptContext(schemes=["sha256_crypt"])

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    def password_validation(self,password: str):
        if not 8 <= len(password) <= 32:
            return False
        
        if re.search(r'(123|abc|qwerty)', password, re.IGNORECASE):
            return False
        
        return True


    def create_user(self, user: userSchema.CreateUser, db: Session):
        # check if username exists
        existing_user = db.query(UserModal).filter(UserModal.username == user.username).first()
        if existing_user:
            raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this username already exists",
        )
        if self.password_validation(user.password) == False:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Password should be atleast 8 characters long and include at least one uppercase, lowercase and a special character. It should not follow sequences like 1234, abc etc"
            )
        # get hashed password
        hashed_password = self.get_password_hash(user.password)
        # add to database
        db_user = UserModal(
            username = user.username,
            password = hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def login_user(self, user:userSchema.CreateUser, db: Session):
        # validate username and password
        existing_user = db.query(UserModal).filter(UserModal.username == user.username).first()
        if existing_user and self.verify_password(user.password, existing_user.password) == True:
            # make a jwt token using secret key and return it
            access_token = self.create_access_token({
                "username":user.username
            })
            return {
                "response":f"{existing_user.username} is logged in succesfully",
                "access_token":access_token
            }
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong username and password combination"
            )