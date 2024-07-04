from processor import message_processing as mp
from model import payment as payment
from model.type_message_variables import TypeMessageVariables as TMV

PaymentMessages = {
    "TypeMessage": TMV.TYPE_MESSAGE_CREATED.value,
    "UidMessage": "1A",
    "AddresFrom": "123",
    "AddresTo": "321",
    "Amount": 50
    }

s = mp.processing(TMV.TYPE_MESSAGE_CREATED.value, "1A", "123", "321", 50)

print(s)
