
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to the Bank")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))

        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Please enter a valid amount")

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))

        if amount <= 0:
            print("Please enter a valid amount")
        elif self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Net available balance =", self.balance)


