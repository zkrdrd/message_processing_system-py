from model import message_payment as mP
from model.error_tracking import ValidationError
from storage.memory.db import MemoryDataBase as MDB

def processing(TM, UM, AF, AT, A) -> str:
    he = mP.MessagePayment(TM, UM, AF, AT, A)
    s = he.get_message_payment()
    MDB.init_memory_base
    MDB.insert_to_memory
    MDB.get_message_payment(UM)
    return s

