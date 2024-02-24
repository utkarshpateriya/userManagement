from fastapi import APIRouter, Body
from utils.justforfunUtils import JustForFunUtil

router = APIRouter()

@router.post('/flattenDict')
def flattenDict(data: dict= Body(...)):
    justforfunObj = JustForFunUtil()
    return justforfunObj.flatten_the_dict(data)