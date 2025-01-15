from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str = None
    price: int
    
    
class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    
    class config:
        orm_mode = True