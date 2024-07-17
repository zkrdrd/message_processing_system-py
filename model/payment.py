from datetime import datetime
from parameters.constants import Constants

class Payment:

    type_message:str
    uid_message:str
    addres_from:str
    addres_to:str
    amount:int
    created_at:str
    updated_at:str

    def __init__(self, type_message, uid_message, 
                 addres_from, addres_to, amount) -> None:    
        self.type_message = type_message
        self.uid_message = uid_message
        self.addres_from = addres_from
        self.addres_to = addres_to
        self.amount = amount
        self.created_at = self.set_datetime()
        self.updated_at = self.set_datetime()

    def set_datetime(self):
        return datetime.now().strftime(Constants.DATE_TIME.value)
    
    def get_uid_message(self):
        return self.uid_message

    def get_message_payment(self) -> str:
        return self.type_message, self.uid_message, self.addres_from, self.addres_to, self.amount, self.created_at, self.updated_at
    
    def set_payment(self, created_at, updated_at):
        self.created_at = created_at
        self.updated_at = updated_at