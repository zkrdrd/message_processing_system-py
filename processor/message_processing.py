from model import message_payment as mP
import storage.memory.db as db 
from model.payment import Payment
from model.message_payment import MessagePayment

class Processing:
    def processing() -> str:
        MessagePayment().ToPayment()

        #mP.MessagePayment()
        #db.init_memory_base()
        #db.insert_to_memory()
        #db.get_payment_dy_id()

    # return s

