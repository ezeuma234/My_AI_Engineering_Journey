class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self):
     try:
        amount = int(input("Amount: "))
     except ValueError:
        print("Invalid Amount")
     else:
      if amount > self.balance:
        print("Insufficient funds")
      else:
         self.balance -= amount
         print("Withdrawal successful")
     finally:
      print("Transaction complete")

    def show_balance(self):
      print("Remaining balance:", self.balance)
       

account1 = BankAccount("Uma", 50000)

account1.withdraw()
account1.show_balance()
