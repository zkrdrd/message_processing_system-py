from model.payment import Payment

class StorageInMemory:

    def __init__(self):
        self.memory_database = {}
        #return self.memory_database

    def save_payment(self, payment:Payment):
        print(payment.get_uid_message)
        #print(s)
        #self.memory_database[payment.uid_message] = payment.get_message_payment()

    def get_payment_dy_id(self, id:str):
        if id in self.memory_database:
            print("yes")
            obj = Payment
            get = obj.get_message_payment()
            print(get)
        else:
            print("no")
