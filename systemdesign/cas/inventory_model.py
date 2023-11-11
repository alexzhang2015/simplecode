from sqlalchemy import Column, Integer 
from sqlalchemy.orm import declarative_base

Base = declarative_base() 

class Inventory(Base):
    __tablename__ = 'inventory'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    total = Column(Integer)