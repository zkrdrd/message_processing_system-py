from model.Payment import Payment

class MessagePayment(Payment):
    
    def __init__(self,
                 TypeMessage,
                 UidMessage,
                 AddresFrom,
                 AddresTo,
                 Amount) -> None:
        Payment.SetMessagePaymentToPayment(self,
                                           TypeMessage,
                                           UidMessage,
                                           AddresFrom,
                                           AddresTo,
                                           Amount)



