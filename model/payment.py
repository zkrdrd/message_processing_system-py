from datetime import datetime


class Payment:

    # TypeMessage:str
    # UidMessage:str
    # AddresFrom:str
    # AddresTo:str
    # Amount:int

    def set_message_to_payment(self, type_message, uid_message,
                               addres_from, addres_to, amount) -> None:    
        self.type_message = type_message
        self.uid_message = uid_message
        self.addres_from = addres_from
        self.addres_to = addres_to
        self.amount = amount
        self.created_at = self.set_date_time()
        self.updated_at = self.set_date_time()

    def set_date_time(self) -> None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def get_uid_message(self):
        return self.uid_message

    def get_message_payment(self) -> str:
        return self.type_message, self.uid_message, self.addres_from, self.addres_to, self.amount, self.created_at, self.updated_at