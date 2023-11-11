from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from inventory_model import Inventory, Base

engine = create_engine('sqlite:///test.db', echo=True)

Base.metadata.create_all(engine) 

def init_db():
    session = Session(bind=engine)
    session.add(Inventory(product_id=1, total=100))
    session.commit()