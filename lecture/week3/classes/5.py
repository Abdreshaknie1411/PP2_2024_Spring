class Account:
    percentage=1.15
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self):
        self.balance=self.balance*self.percentage
        return self.balance
    def withdrawals(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            return self.balance
owner=str(input())
balance=int(input())
my_acc=Account(owner,balance)
print(my_acc.deposit())
print(my_acc.withdrawals())