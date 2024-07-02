from model.Payment import Payment
from model.TypeMessageVariables import TypeMessageVariables as TMP

class MessagePayment(Payment):
    
    def __init__(self, TypeMessage, UidMessage,
                 AddresFrom, AddresTo, Amount) -> None:

        validation = self.ValidateRequiredFields(TypeMessage, UidMessage)
        if validation != None:
            print(validation)
            exit()

        Payment.SetMessagePaymentToPayment(self, TypeMessage, UidMessage,
                                           AddresFrom, AddresTo, Amount)


    def ValidateRequiredFields(self, TypeMessage, UidMessage) -> str:
        
        if not TypeMessage:
            return 'Fiend "TypeMessage" is empty'

        if not UidMessage:
            return 'Field "UidMessage" is empry'

        if (TypeMessage != TMP.TYPE_MESSAGE_CREATED.value and
            TypeMessage != TMP.TYPE_MESSAGE_PROCESSED.value and
            TypeMessage != TMP.TYPE_MESSAGE_CANCELED.value):
            return 'Field "TypeMessage" is not correct'
        

