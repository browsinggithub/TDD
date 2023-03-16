class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit_money(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount
        
class Bank:
    def open_account(self, name):
        return Account(name)


