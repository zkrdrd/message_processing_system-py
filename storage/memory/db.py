from models.payment import Payment

class StorageInMemory:

    def __init__(self) -> None:
        """Инициализация хранилища"""
        self.__memory_database = {}

    def save_payment(self, payment:Payment) -> None:
        """Сохранение данных в хранилище"""
        self.__memory_database[payment.uid_message] = payment

    def get_payment_by_id(self, id:str) -> Payment:
        """Получение данных из хранилища по id"""
        if id in self.__memory_database:
            #print(vars(self.memory_database[id]))
            return self.__memory_database[id]
        else:
            return None