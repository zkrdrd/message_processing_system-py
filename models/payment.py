from datetime import datetime

DATE_TIME = "%d-%m-%Y %H:%M:%S"


class Payment:

    def __init__(
        self,
        type_message: str,
        uid_message: str,
        address_from: str,
        address_to: str,
        amount: int,
    ) -> None:
        """Констурктор класса Payment"""
        self.type_message = type_message
        self.uid_message = uid_message
        self.address_from = address_from
        self.address_to = address_to
        self.amount = amount
        self.created_at = self.get_formatted_datetime()
        self.updated_at = self.created_at

    # def update_updated_at(self):
    #    self.updated_at = self.__get_formatted_datetime()

    @staticmethod
    def get_formatted_datetime() -> str:
        """Получение времени определенного формата"""
        return datetime.now().strftime(DATE_TIME)

    def get_uid_message(self) -> str:
        """Получение поля uid_message"""
        return self.uid_message
