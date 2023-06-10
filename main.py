from user import User
Abul = User("Abul Mia")
Rahim = User("Rahim Mia")

# Perform operations
Abul.deposit(1000)
Abul.check_balance()

Rahim.deposit(7000)
Rahim.check_balance()

Abul.transfer(Rahim, 500)
Abul.check_balance()
Rahim.check_balance()