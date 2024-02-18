from passlib.context import CryptContext
from schemas import userSchema

class UserUtils:

    def get_password_hash(self, password: str):
        pwd_context = CryptContext(schemes=["sha256_crypt"])
        return pwd_context.hash(password)
    
    def create_user(user: userSchema.CreateUser, db):
        # check if username exists
        # get hashed password
        # add to database
        pass