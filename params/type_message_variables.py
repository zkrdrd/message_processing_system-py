from enum import Enum


class TypeMessageVariables(Enum):
    TYPE_MESSAGE_CREATED = "created"
    TYPE_MESSAGE_PROCESSED = "processed"
    TYPE_MESSAGE_CANCELED = "canceled"
