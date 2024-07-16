from model.payment import Payment

class MessagePayment():

    type_message:str
    uid_message:str
    addres_from:str
    addres_to:str
    amount:int
    
    def __init__(self, type_message, uid_message,
                 addres_from, addres_to, amount) -> None:
        self.type_message = type_message
        self.uid_message = uid_message
        self.addres_from = addres_from
        self.addres_to = addres_to
        self.amount = amount
    
    def to_payment(self) -> Payment:
        return Payment(self.type_message, self.uid_message, self.addres_from, self.addres_to, self.amount)


    