from model.payment import Payment
from model.error_tracking import ValidationError

class MessagePayment(Payment, ValidationError):
    
    def __init__(self, type_message, uid_message,
                 addres_from, addres_to, amount) -> None:

        #type_message=""
        try:
            ValidationError.validate_required_fields(self, type_message, uid_message)
        except ValidationError as err:
            print(err)
            exit()

        Payment.set_message_payment_to_payment(self, type_message, uid_message,
                                           addres_from, addres_to, amount)

    
    