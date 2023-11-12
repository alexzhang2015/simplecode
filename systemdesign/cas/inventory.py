from asyncio import InvalidStateError
from sqlalchemy import func
from database import Session
from inventory_model import Inventory

# 同样的CAS逻辑代码


def reduce_cas(session: Session, product_id: int, num: int) -> bool:
    try:

        # 获取锁定记录
        inventory = session.query(Inventory)\
            .filter(Inventory.product_id == product_id)\
            .with_for_update()\
            .first()

        # 读取库存值
        old_total = inventory.total

        # 判断库存是否足够
        if old_total < num:
            return False

        # CAS更新
        updated = session.query(Inventory) \
            .filter(Inventory.total == old_total, Inventory.product_id == product_id) \
            .update({Inventory.total: old_total - num})

        if updated > 0:
            session.commit()
            return True

        session.rollback()
        return False

    except InvalidStateError:
        pass
