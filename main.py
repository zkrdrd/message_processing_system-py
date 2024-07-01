from internal.processor import message_processing as mp
from model import Payment as payment

PaymentMessages = {
    "TypeMessage": payment.TYPE_MESSAGE_CREATED,
    "UidMessage": "1A",
    "AddresFrom": "123",
    "AddresTo": "321",
    "Amount": 50
    }

s = mp.Processing(payment.TYPE_MESSAGE_CREATED, "1A", "123", "321", 50)

print(s)

