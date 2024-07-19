from params.type_message_variables import TypeMessageVariables as TMP

class ValidationError(Exception):

    def validate_required_fields(self, type_message, uid_message) -> Exception:
        """Проверка коректности обязательных полей для записи новых и обновления старых записей"""
        
        if not type_message:
            raise ValidationError('ValidationError: field "TypeMessage" is empty')

        if not uid_message:
            raise ValidationError('ValidationError: field "UidMessage" is empty')

        if (type_message != TMP.TYPE_MESSAGE_CREATED.value and
            type_message != TMP.TYPE_MESSAGE_PROCESSED.value and
            type_message != TMP.TYPE_MESSAGE_CANCELED.value):
            raise ValidationError('ValidationError: field "TypeMessage" is not correct')
        
    def validate_requred_field_for_new_save_db(self, address_to, address_from, amount) -> Exception:
        """Проверка обязательных полей для новой записи"""

        if not address_to:
            raise ValidationError('ValidationError: field "AddresTo" is empty')
        if not address_from:
            raise ValidationError('ValidationError: field "AdressFrom" is empty')
        if amount <= 0:
            raise ValidationError('ValidationError: field "Amount" is less or equal zero')
        
    def validate_field_type_message_for_update_db(self, type_message) -> Exception:
        """Проверка поля type_message что бы не менять стус ранее исполненного статуса на 'Изменен', 'Отменен'"""
        if type_message != TMP.TYPE_MESSAGE_CREATED.value:
            raise ValidationError(f'ValidationError: payment with this UID is exist in storage')
        
    def check_dublicate_payment_in_storage(self, payment_type_message, message_payment_type_message) -> Exception:
        """Проверка поля type_message для проверки на дубликат записи"""
        if payment_type_message == message_payment_type_message:
            raise ValidationError(f'ValidationError: payment is dublicate')
