from model import message_payment as mP
import storage.memory.db as db 
from model.payment import Payment
from model.message_payment import MessagePayment
from storage.memory.db import StorageInMemory
from model.error_tracking import ValidationError

class Processing:
    def processing(msg:MessagePayment) -> str:
#TODO:
# 1. исправить инийиализацию новой базы in memory при каждой итерации
        obj_storage_memory = StorageInMemory()
        
        payment = obj_storage_memory.get_payment_dy_id(msg.uid_message)
        if payment.uid_message == None:
            try:
                ValidationError().validate_requred_field_for_new_save_db(msg.addres_to, msg.addres_from, msg.amount)
            except ValidationError as err:
                print(err)
            else:
                if err := obj_storage_memory.save_payment(msg.to_payment()):
                    print(err)
        else:
            try:
                ValidationError().validate_field_type_message_for_update_db(payment.type_message)
            except ValidationError as err:
                print(err)
            else: 
                payment.type_message = msg.type_message
                if err := obj_storage_memory.save_payment(payment):
                    print(err)



        payment = obj_storage_memory.get_payment_dy_id(msg.uid_message)
        if payment.uid_message != None:
            print("ok")


