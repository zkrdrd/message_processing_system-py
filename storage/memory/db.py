from model.payment import Payment

class StorageInMemory:

    def __init__(self):
        self.memory_database = {}

    def save_payment(self, payment:Payment):
        self.memory_database[payment.uid_message] = payment

    def get_payment_dy_id(self, id:str) -> Payment:
        if id in self.memory_database:
            print(vars(self.memory_database[id]))
            return self.memory_database[id]
        else:
            return None