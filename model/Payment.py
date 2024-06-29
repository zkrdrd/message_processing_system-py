from model.MessagePayment import MessagePayment
from datetime import datetime


class Payment(MessagePayment):

    def SetCreatedAt(self):
        self.CreatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def SetUpdatedAt(self):
        self.UpdatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def GetCreatedAt(self):
        return self.CreatedAt
    
    def GetUpdatedAt(self):
        return self.UpdatedAt
