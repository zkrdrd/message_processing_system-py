from abc import ABC
from abc import abstractmethod
from models.payment import Payment

class Storage(ABC):

    @abstractmethod
    def new_storage(self):
        pass

    @abstractmethod
    def save_payment(self, _:Payment):
        pass

    @abstractmethod
    def get_payment_by_id(_:str):
        pass