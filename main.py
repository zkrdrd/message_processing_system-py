import sqlite3
from time import sleep
from log.logger import logger
from models.message_payment import MessagePayment
from get_env.get_enviroment import Environment
from error_tracking.env_error import EnvError
from processor.message_processing import Processing
from params.type_message_variables import TypeMessageVariables
from error_tracking.validation_error import ValidationError

PaymentMessages = [
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "123", "321", 50),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_PROCESSED.value, "1A", "", "", ""),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CANCELED.value, "1A", "", "", ""),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "525", "1512", 2345),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "", "", "")
]

storage_type, storage_file_path = Environment().get_env_storage()
storage = Environment().use_storage(storage_type, storage_file_path)
if isinstance(storage,EnvError):
    exit()

for msg in PaymentMessages:
    #msg.type_message = ""
    try:
        ValidationError().validate_required_fields(msg.type_message, msg.uid_message)
    except ValidationError as err:
        logger.error(err)
    else:
        sleep(5)
        msg.to_payment()
        payment = Processing.processing(msg, storage)
        print(type(payment))
        if isinstance(payment,sqlite3.Error):
            exit()
    