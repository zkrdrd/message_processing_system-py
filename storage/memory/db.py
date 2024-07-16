from model.payment import Payment

class StorageInMemory:

    def __init__(self):
        self.memory_database = {}

    def save_payment(self, payment:Payment):
        self.memory_database[payment.uid_message] = payment.get_message_payment()

#TODO: 
# 1. Eсли запись есть поменять статус 
    def get_payment_dy_id(self, id:str) -> Payment:
        #obj = Payment()
        if id in self.memory_database:
            print(self.memory_database[id])
            for val in self.memory_database.values():
                return Payment(val[0], val[1], val[2], val[3], val[4]).set_payment(val[5], val[6])
        else:
            return Payment(None, None, None, None, None)