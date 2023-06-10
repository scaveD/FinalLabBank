from bank import Bank 
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []
        self.loanTaken = False

    def deposit(self, amount):
        Bank.deposit(self, amount)
        self.transactions.append(f"Deposited {amount}Taka")

    def withdraw(self, amount):
        Bank.withdraw(self, amount)
        self.transactions.append(f"Withdrew {amount}Taka")

    def transfer(self, receiver, amount):
        Bank.transfer(self, receiver, amount)
        self.transactions.append(f"Transferred {amount}Taka to {receiver.name}'s account")

    def takeLoan(self):
        Bank.takeLoan(self)
        self.transactions.append("loan taken")

    def check_balance(self):
        print(f"Currently available balance for {self.name}: {self.balance}Taka")

    def chkTransactiton(self):
        Bank.chkTransactiton(self)