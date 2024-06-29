import string

class MessagePayment:
    def __init__(self,
                 TypeMessage,
                 UidMessage,
                 AddresFrom,
                 AddresTo,
                 Amount):    
        self.TypeMessage = TypeMessage
        self.UidMessage = UidMessage
        self.AddresFrom = AddresFrom
        self.AddresTo = AddresTo
        self.Amount = Amount

    def GetMessagePaymentTypeMessage(self):
        return self.TypeMessage
    
    def GetMessagePaymentUidMessage(self):
        return self.UidMessage
    
    def GetMessagePaymentAddresFrom(self):
        return self.AddresFrom
    
    def GetMessagePaymentAddresTo(self):
        return self.AddresTo
    
    def GetMessagePaymentAmount(self):
        return self.Amount

    def GetMessagePayment(self):
        return self.TypeMessage, self.UidMessage, self.AddresFrom, self.AddresTo, self.Amount

