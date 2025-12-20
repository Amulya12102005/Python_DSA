class Bank:
    def __init__(self,amount):
        self.balance=amount
    def debit(self,amount):
        self.debit==amount
        print("amount debited:",amount)
        print("Total:",self.balance)
    def credit(self,amount):
        self.balance=amount
        print("amount credited:",amount)
        print("Total:",self.balance)
user=Bank(100)
print(user.balance)
user.credit(600)
user.debit(700)