from model.Payment import Payment
from model.TypeMessageVariables import TypeMessageVariables as TMP
import inspect

class MessagePayment(Payment):
    
    def __init__(self, TypeMessage, UidMessage,
                 AddresFrom, AddresTo, Amount) -> None:

        TypeMessage=""

        validation = self.ValidateRequiredFields(TypeMessage, UidMessage)
        if validation != None:
            print(validation)
            exit()

        Payment.SetMessagePaymentToPayment(self, TypeMessage, UidMessage,
                                           AddresFrom, AddresTo, Amount)

    # Проверка коректности обязательных полей
    def ValidateRequiredFields(self, TypeMessage, UidMessage) -> str:
        
        if not TypeMessage:
            return self.ErrFieldIsEmpty("TypeMessage")

        if not UidMessage:
            return self.ErrFieldIsEmpty("UidMessage")

        if (TypeMessage != TMP.TYPE_MESSAGE_CREATED.value and
            TypeMessage != TMP.TYPE_MESSAGE_PROCESSED.value and
            TypeMessage != TMP.TYPE_MESSAGE_CANCELED.value):
            return self.ErrFieldIsNotCorrect("TypeMessage")
        
    # Возвращает ошибки если поле путое
    def ErrFieldIsEmpty(self, field) -> str:
        return (f'Field "{field}" is empry')
    
    # Возвращает ошибку елси поле имеет не верные данные 
    def ErrFieldIsNotCorrect(self, field) -> str:
        return (f'Field "{field}" is not correct')