from model.payment import Payment

class StorageInMemory:

    def __init__(self):
        self.memory_database = {}

    def save_payment(self, payment:Payment):
        self.memory_database[payment.uid_message] = payment.get_message_payment()

    def get_payment_dy_id(self, id:str):
        if id in self.memory_database:
            print("yes")
            print(self.memory_database[id])
            for val in self.memory_database.values():
                return Payment(val[0], val[1], val[2], val[3], val[4])
        else:
            print("no")
