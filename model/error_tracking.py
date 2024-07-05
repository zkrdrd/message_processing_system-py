
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
        
