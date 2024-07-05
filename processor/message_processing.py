from model import message_payment as mP
from model.error_tracking import ValidationError
from storage.memory.db import MemoryDataBase as MDB

def processing(TM, UM, AF, AT, A) -> str:
    mP.MessagePayment(TM, UM, AF, AT, A)

    obj = MDB()
    obj.init_memory_base()
    obj.insert_to_memory()
    obj.get_payment_dy_id(UM)

   # return s

