from model.payment import Payment

class StorageInMemory:
    def init_memory_base():
        memory_database = []
        return memory_database

    def save_payment(self, payment:Payment):
        obj = Payment
        print(obj.get_uid_message())
        #self.memory_database[super().uid_message] = obj.get_message_payment()

    def get_payment_dy_id(memory_database, id:str) -> object:
        if id in memory_database:
            obj = Payment
            get = obj.get_message_payment()
            print(get)
        else:
            print("no")
