class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Deposited", amount)

    def withdraw(self, amount):
     if amount > self.balance:
        print("Insufficient funds")
     else:
        self.balance -= amount

    def show_balance(self):
        print(self.owner)
        print(self.balance)

account1 = BankAccount("Uma", 200000)
account2 = BankAccount("Eileen", 400000)

account1.deposit(10000)
account1.withdraw(5000)
account1.show_balance()
