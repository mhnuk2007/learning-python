""" Encapsulation Example: Bank Account """

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Demo
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance accessed safely:", acc.get_balance())
# print(acc.__balance)  # Would raise AttributeError