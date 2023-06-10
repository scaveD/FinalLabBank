class Bank:
    total_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

    @classmethod
    def getTotalBalance(self):
        return self.total_balance

    @classmethod
    def getTotalLoan(self):
        return self.total_loan_amount

    @classmethod
    def ActiveLoanFeature(self):
        self.loan_feature_enabled = True
        print("Loan feature activated.")

    @classmethod
    def DeactiveLoanFeature(self):
        self.loan_feature_enabled = False
        print("Loan feature deactivated.")

    @classmethod
    def deposit(self, user, amount):
        if amount <= 0:
            print("Sorry invalid amount.")
            return
        user.balance += amount
        self.total_balance += amount
        print(f"Deposited {amount}Taka into {user.name}'s account.")

    @classmethod
    def withdraw(self, user, amount):
        if amount <= 0:
            print("Not posible")
            return
        if user.balance >= amount:
            user.balance -= amount
            self.total_balance -= amount
            print(f"Withdrewed {amount}Taka from {user.name}'s account.")
        else:
            print("CAution! Balance insufficient.")

    @classmethod
    def transfer(self, sender, receiver, amount):
        if amount <= 0:
            print("This amount can't be transfered.")
            return
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            print(f"Transaction successful. Transfered {amount}Taka from {sender.name}'s account to {receiver.name}'s account.")
        else:
            print("This amount can't be transfered.")

    @classmethod
    def takeLoan(self, user):
        if not self.loan_feature_enabled:
            print("The loan feature is currently deacttivated by admin.")
            return
        if user.loanTaken:
            print("Debt ! Can't take loan")
            return
        loan_amount = 2 * user.balance
        user.balance += loan_amount
        self.total_loan_amount += loan_amount
        user.loanTaken = True
        print(f"You have successfully taken a loan of {loan_amount}Taka. The amount has been added to your account.")

    @classmethod
    def chkTransactiton(self, user):
        print(f"Transaction log of {user.name}:")
        for transaction in user.transactions:
            print(transaction)