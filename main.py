from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database, crud

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

#path parameters and query parameters
# @app.get("/users/{user_id}/items/{item_id}")
# def read_user_item(user_id: int, item_id: int, detail:str = None):
#     return {
#             "user_id": user_id, 
#             "item_id": item_id, 
#             "detail": detail, 
#             }

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    print(item)
    return crud.create_item(db=db, item=item)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item