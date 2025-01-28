from models.payment import Payment


class Storage:

    def __init__(self) -> None:
        self.storage = object

    @classmethod
    def new_storage(self, storage: object):
        self.__storage = storage

    @classmethod
    def get_storage(self) -> object:
        return self.__storage

    def save_payment(payment: Payment) -> None:
        pass

    def get_payment_by_id(id: str) -> object:
        pass
