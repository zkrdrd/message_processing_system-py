from processor.message_processing import Processing
from model.payment import Payment
from model.type_message_variables import TypeMessageVariables
from model.message_payment import MessagePayment
from model.error_tracking import ValidationError
import logging

file_log = logging.FileHandler('logging.log')
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

PaymentMessages = [
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "123", "321", 50),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_PROCESSED.value, "1A", "", "", ""),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CANCELED.value, "1A", "", "", ""),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "525", "1512", 2345),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "", "", "")
]

for msg in PaymentMessages:
    #msg.type_message = ""
    try:
        ValidationError().validate_required_fields(msg.type_message, msg.uid_message)
    except ValidationError as err:
        logging.info(err)
    else:
        msg.to_payment()
        Processing.processing(msg)
    