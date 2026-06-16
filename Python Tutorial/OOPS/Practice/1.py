class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        print(f"Rs. {amount} deposit successfully.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Insufficient Balance")

    def checkBalance(self):
        print(f"current Balance: Rs.{self.balance}")

# creating an object
account1 = BankAccount("1234" , "Abhishek", 12000 )

account1.checkBalance()
account1.deposit(2000)
account1.checkBalance()
account1.withdraw(8000)
account1.checkBalance()
        