import random

def StringSeperator(TheString):
    NewArray = TheString.split()
    rand =  random.randint(0,5)
    return NewArray[rand]



TheString = "Hello My Name is Saibrath Silwal"
print(StringSeperator(TheString))
