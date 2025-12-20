class Bank:
    def __init__(self, amount):
        self.balance = amount
    def debit(self, amount):
        self.balance -= amount
        print("Amount debit:", amount)
        print("total :",self.balance())
    def credit(self, amount):
        self.balance += amount
        print("Amount credit:",amount)
        print("total :",self.balance())
    def balance(self):
        return self.balance
user=Bank(100)
user.debit(100)
user.debit(100)


