class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #private access
    
    # def get_info(self):
    #     print(f"Name is: {self.name} and balance is: {self._balance}")

    def get_balance(self):  #getter method
        return self.__balance
    
    def set_balance(self, new_balance): #setter
        self.__balance = new_balance


acc1 = Bank("Abhishek", 50000)
acc2 = Bank("Karan", 40000)

# acc1.get_info()
# print(acc1.name, acc1.__balance)
# print(acc1.name , acc1.get_balance())

acc1.set_balance(200000)
print(acc1.name , acc1.get_balance())