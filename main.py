from processor.message_processing import Processing
from parameters.type_message_variables import TypeMessageVariables
from model.message_payment import MessagePayment
from error_tracking.validation_error import ValidationError
from parameters.enviroment import Environment
from log.logger import logger

#log = logging.getLogger()

PaymentMessages = [
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "123", "321", 50),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_PROCESSED.value, "1A", "", "", ""),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CANCELED.value, "1A", "", "", ""),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "525", "1512", 2345),
    MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "", "", "")
]

storage_type, storage_file_path = Environment.get_env_storage()
storage = Environment.use_storage(storage_type, storage_file_path)


for msg in PaymentMessages:
    #msg.type_message = ""
    try:
        ValidationError().validate_required_fields(msg.type_message, msg.uid_message)
    except ValidationError as err:
        logger.error(err)
    else:
        msg.to_payment()
        Processing.processing(msg, storage)
    