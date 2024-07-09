from model.payment import Payment


def init_memory_base():
    memory_database = {}
    return memory_database

def insert_to_memory():
    obj = Payment
    print(obj.get_uid_message())
    #self.memory_database[super().uid_message] = obj.get_message_payment()

def get_payment_dy_id(memory_database, id) -> object:
    if id in memory_database:
        obj = Payment
        get = obj.get_message_payment()
        print(get)
    else:
        print("no")