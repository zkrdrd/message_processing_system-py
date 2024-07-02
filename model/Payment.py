from datetime import datetime


class Payment:

    # TypeMessage:str
    # UidMessage:str
    # AddresFrom:str
    # AddresTo:str
    # Amount:int

    def SetMessagePaymentToPayment(self, TypeMessage, UidMessage,
                                   AddresFrom, AddresTo, Amount) -> None:    
        self.TypeMessage = TypeMessage
        self.UidMessage = UidMessage
        self.AddresFrom = AddresFrom
        self.AddresTo = AddresTo
        self.Amount = Amount
        self.SetCreatedAt()
        self.SetUpdatedAt()

    def SetCreatedAt(self) -> None:
        self.CreatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def SetUpdatedAt(self) -> None:
        self.UpdatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def GetMessagePaymentTypeMessage(self) -> str:
        return self.TypeMessage
    
    def GetMessagePaymentUidMessage(self) -> str:
        return self.UidMessage
    
    def GetMessagePaymentAddresFrom(self) -> str:
        return self.AddresFrom
    
    def GetMessagePaymentAddresTo(self) -> str:
        return self.AddresTo
    
    def GetMessagePaymentAmount(self) -> int:
        return self.Amount

    def GetCreatedAt(self) -> str:
        return self.CreatedAt
    
    def GetUpdatedAt(self) -> str:
        return self.UpdatedAt
    
    def GetMessagePayment(self) -> str:
        return self.TypeMessage, self.UidMessage, self.AddresFrom, self.AddresTo, self.Amount, self.CreatedAt, self.UpdatedAt