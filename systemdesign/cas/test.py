from asyncio import InvalidStateError
from concurrent.futures import ThreadPoolExecutor

from database import init_db, Session, engine  
from inventory import reduce_cas
from inventory_model import Inventory

init_db()

def test(product_id, num):
    session = Session(bind=engine) 
    reduce_cas(session, product_id, num)
    session.close()

# with Session(bind=engine) as session:
#    test(session, 1, 10)

# 启动线程池测试    
with ThreadPoolExecutor() as executor:
    futures = executor.map(test, [1]*10, [10]*10)
    try:
        for _ in futures: pass
    except InvalidStateError:
        pass 
   
with Session(bind=engine) as session:
   print(session.query(Inventory).filter(Inventory.product_id==1).first().total)