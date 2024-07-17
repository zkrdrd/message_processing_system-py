from log.logger import logger
from model.message_payment import MessagePayment
from error_tracking.validation_error import ValidationError

class Processing:

    def processing(msg:MessagePayment, storage) -> str:
    #TODO:
    # 1. исправить инийиализацию новой базы in memory при каждой итерации
        #obj_storage_memory = StorageInMemory()
        
        payment = storage.get_payment_dy_id(msg.uid_message)        
        if payment.uid_message == None:
            try:
                ValidationError().validate_requred_field_for_new_save_db(msg.addres_to, msg.addres_from, msg.amount)
            except ValidationError as err:
                logger.error(err)
            else:
                if err := storage.save_payment(msg.to_payment()):
                    logger.error(err)
        else:
            try:
                ValidationError().validate_field_type_message_for_update_db(payment.type_message)
            except ValidationError as err:
                logger.error(err)
            else: 
                payment.type_message = msg.type_message
                payment.updated_at = payment.set_datetime()
                if err := storage.save_payment(payment):
                    logger.error(err)



        payment = storage.get_payment_dy_id(msg.uid_message)
        if payment != None:
            if payment.uid_message != None:
                print("ok")
