import datetime

class price:
    def __init__(self, amount):
        self.date = datetime.date.today()
        self.amount = amount 

class item:
    def __init__(self, name, upc, prices=[]):
        self.name = name
        self.upc = upc 
        self.prices = prices 

