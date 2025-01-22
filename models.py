from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items" 
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    
    # @field_validator('email')
    # def validate_email(cls, v):
    #     if "@" not in v:
    #         raise ValueError("Invalid email")
    #     return v