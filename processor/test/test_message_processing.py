from time import sleep
from log.logger import logger
from models.payment import Payment
from storage.memory.db import StorageInMemory
from models.message_payment import MessagePayment
from processor.message_processing import Processing
from params.type_message_variables import TypeMessageVariables
from error_tracking.validation_error import ValidationError

STORAGE = StorageInMemory()

def processor(PaymentMessages:MessagePayment):
    try:
        ValidationError().validate_required_fields(PaymentMessages.type_message, PaymentMessages.uid_message)
    except ValidationError as err:
        logger.error(err)
        return err
    else:
        sleep(5)
        PaymentMessages.to_payment()
        err = Processing.processing(PaymentMessages, STORAGE)
    return err

# 1
def test_processor_validation_error_1():
    """type_message is empty"""
    assert isinstance(processor(MessagePayment("", "1A", "123", "321", 50)), ValidationError)

# 2
def test_processor_validation_error_2():
    """uid_message is empty"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "", "123", "321", 50)), ValidationError)

# 3
def test_processor_validation_error_3():
    """address_from is empty"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "", "321", 50)), ValidationError)

# 4
def test_processor_validation_error_4():
    """address_to is empry"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "123", "", 50)), ValidationError)

# 5
def test_processor_validation_error_5():
    """amount <= 0"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "123", "321", -10)), ValidationError)

# 6
def test_processor_return_value_1():
    """it is OK, return payment"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "1A", "123", "321", 50)), Payment)

# 7
def test_processor_return_value_2():
    """it is OK, return payment"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_PROCESSED.value, "1A", "", "", "")), Payment)

# 8
def test_processor_validation_is_updated_1():
    """it is updated early"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CANCELED.value, "1A", "", "", "")), ValidationError)

# 9
def test_processor_return_value_3():
    """it is OK, return payment"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "525", "1512", 2345)), Payment)

# 10 
def test_processor_validation_is_dublicate_1():
    """it is dublicate payment"""
    assert isinstance(processor(MessagePayment(TypeMessageVariables.TYPE_MESSAGE_CREATED.value, "2A", "", "", "")), ValidationError)