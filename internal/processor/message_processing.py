from model import MessagePayment as mP

def Processing(TM, UM, AF, AT, A) -> str:
    he = mP.MessagePayment(TM, UM, AF, AT, A)
    s = he.GetMessagePayment()
    return s

