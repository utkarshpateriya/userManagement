from fastapi import FastAPI, Depends
from schemas import Item as ItemSchema
from utils import create_item, make_word_list

from database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def root():
    return {"app":"working"}

@app.get('/wordcount')
def countWord(item: ItemSchema):
    return make_word_list(item.description)

@app.post('/createItem')
def createItem(item:ItemSchema, db:Session = Depends(get_db)):
    return create_item(db, item)

@app.get("/listallitems")
async def listItems():
    pass