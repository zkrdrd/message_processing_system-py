
from model.type_message_variables import TypeMessageVariables as TMP

class ValidationError(Exception):

    # Проверка коректности обязательных полей
    def validate_required_fields(self, type_message, uid_message) -> str:
        
        if not type_message:
            raise ValidationError('ValidationError: field "TypeMessage" is empty')

        if not uid_message:
            raise ValidationError('ValidationError: field "UidMessage" is empty')

        if (type_message != TMP.TYPE_MESSAGE_CREATED.value and
            type_message != TMP.TYPE_MESSAGE_PROCESSED.value and
            type_message != TMP.TYPE_MESSAGE_CANCELED.value):
            raise ValidationError('ValidationError: field "TypeMessage" is not correct')
        
    def validate_requred_field_for_new_save_db(self, addres_to, addres_from, amount) -> str:
        if not addres_to:
            raise ValidationError('ValidationError: field "AddresTo" is empty')
        if not addres_from:
            raise ValidationError('ValidationError: field "AdressFrom" is empty')
        if amount <= 0:
            raise ValidationError('ValidationError: field "Amount" is less or equal zero')
        
    def validate_field_type_message_for_update_db(self, type_message):
        print(type_message)
        if type_message != TMP.TYPE_MESSAGE_CREATED.value:
            raise ValidationError('ValidationError: field "TypeMessage" is not correct')