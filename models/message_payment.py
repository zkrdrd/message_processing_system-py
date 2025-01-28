from models.payment import Payment


class MessagePayment:

    def __init__(
        self,
        type_message: str,
        uid_message: str,
        address_from: str,
        address_to: str,
        amount: int,
    ) -> None:
        """Конструктор класса MessagePayment"""
        self.type_message = type_message
        self.uid_message = uid_message
        self.address_from = address_from
        self.address_to = address_to
        self.amount = amount

    def to_payment(self) -> Payment:
        """Передача полей для инициализации в классе Payment"""
        return Payment(
            self.type_message,
            self.uid_message,
            self.address_from,
            self.address_to,
            self.amount,
        )
