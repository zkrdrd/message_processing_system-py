from model import message_payment as mP
import storage.memory.db as db 
from model.payment import Payment
from model.message_payment import MessagePayment
from storage.memory.db import StorageInMemory

class Processing:
    def processing(msg:MessagePayment) -> str:

        obj = StorageInMemory()
        #StorageInMemory().init_memory_base()
        if err := obj.get_payment_dy_id(msg.uid_message):
            print(err)

        msg.to_payment()

        if err := obj.save_payment(Payment):
            print(err)

        #mP.MessagePayment()
        #db.init_memory_base()
        #db.insert_to_memory()
        #db.get_payment_dy_id()

    # return s

