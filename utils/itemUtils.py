from sqlalchemy.orm import Session
from schemas.itemsSchema import Item as ItemSchema
from models.itemModel import Item as ItemModel

class ItemCrudMethods:
    def make_word_list(description: str) -> dict:
        word_list = {}
        list_word = description.split(" ")
        for word in list_word:
            word = word.lower()
            if word[-1] == ".":
                word = word[0:len(word)-1]
            if word in word_list:
                word_list[word]+=1
            else:
                word_list[word] = 1
        return word_list

    def create_item(db: Session, item: ItemSchema):
        db_item = ItemModel(name=item.name, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    def list_items(db: Session):
        return db.query(ItemModel).all()