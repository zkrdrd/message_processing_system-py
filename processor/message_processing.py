from model import message_payment as mP
from model.error_tracking import ValidationError
import storage.memory.db as db 

def processing(TM, UM, AF, AT, A) -> str:
    mP.MessagePayment(TM, UM, AF, AT, A)

    db.init_memory_base()
    db.insert_to_memory()
    db.get_payment_dy_id(UM)

   # return s

