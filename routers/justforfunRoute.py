from fastapi import APIRouter, Body
from utils.justforfunUtils import JustForFunUtil

router = APIRouter()

@router.post('/flattenDict')
def flattenDict(data: dict= Body(...)):
    justforfunObj = JustForFunUtil()
    return justforfunObj.flatten_the_dict(data)

@router.get('/getTOTP')
def generate_TOTP(secret: str):
    justforfunObj = JustForFunUtil()
    return justforfunObj.generate_totp(secret=secret)