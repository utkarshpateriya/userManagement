from fastapi import APIRouter, Depends
from database import SessionLocal
from schemas.itemsSchema import Item as ItemSchema
from utils.itemUtils import ItemCrudMethods
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["items"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/wordcount')
def countWord(item: ItemSchema):
    return ItemCrudMethods.make_word_list(item.description)

@router.post('/createItem')
def createItem(item:ItemSchema, db:Session = Depends(get_db)):
    return ItemCrudMethods.create_item(db, item)

@router.get("/listallitems")
async def listItems(db:Session = Depends(get_db)):
    return ItemCrudMethods.list_items(db)