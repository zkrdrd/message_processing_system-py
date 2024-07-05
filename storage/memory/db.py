from model.payment import Payment

class MemoryDataBase(Payment):

    def init_memory_base(self):
        self.memory_database = {}

    def insert_to_memory(self):
        obj = Payment
        print(obj.get_uid_message())
        #self.memory_database[super().uid_message] = obj.get_message_payment()

    def get_payment_dy_id(self, id) -> object:
        if id in self.memory_database:
            get = super().get_message_payment()
            print(get)
        else:
            print("no")