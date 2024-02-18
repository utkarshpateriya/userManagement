from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])

def get_password_hash(password: str):
    return pwd_context.hash(password)

print(get_password_hash("Utkarsh"))