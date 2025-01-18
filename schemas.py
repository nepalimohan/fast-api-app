from typing import Optional
from pydantic import BaseModel

#schemas used for data validation and serialization
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None # using optional str for None to avoid sonarqube error
    price: int
    
    
class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    
    class config:
        orm_mode = True