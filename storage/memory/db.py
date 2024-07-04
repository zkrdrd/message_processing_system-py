from model.payment import Payment

class MemoryDataBase(Payment):

    def init_memory_base(self):
        self.memory_database = {}

    def insert_to_memory(self):
        self.memory_database = [super().uid_message] = super().get_message_payment()

    @classmethod
    def get_message_payment(self, id) -> str:
        if id in self.memory_database:
            get = super().get_message_payment()
            print(get)