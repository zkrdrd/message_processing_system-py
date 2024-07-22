import sqlite3
from log.logger import logger
from models.payment import Payment
from models.message_payment import MessagePayment
from error_tracking.validation_error import ValidationError

class Processing():

    @staticmethod
    def processing(msg:MessagePayment, storage) -> None:
        """Функция обработчик.\n
        Валидация, получение, сохранение, обновление данных"""
        payment = storage.get_payment_by_id(msg.uid_message)
        if isinstance(payment, sqlite3.Error):
            return payment
        if payment == None:
            try:
                ValidationError().validate_requred_field_for_new_save_db(msg.address_to, msg.address_from, msg.amount)
            except ValidationError as err:
                logger.error(err)
                return err
            else:
                if err := storage.save_payment(msg.to_payment()):
                    logger.error(err)
                    return err
        else:
            try:
                ValidationError().validate_field_type_message_for_update_db(payment.type_message)
                ValidationError().check_dublicate_payment_in_storage(payment.type_message, msg.type_message)
            except ValidationError as err:
                logger.error(err)
                return err
            else: 
                payment.type_message = msg.type_message
                payment.updated_at = Payment.get_formatted_datetime()
                if err := storage.save_payment(payment):
                    logger.error(err)
                    return err
        return payment
