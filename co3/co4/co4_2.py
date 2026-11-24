class bankaccount:
    def __init__(self, acc_no, name,acc_type, balance=0):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance

    def deposit(self):
        amt=float(input("enter deposit amount:"))
        if amt>0:
            self.balance += amt
            print("deposited:", amt)
        else:
            print("invalid amount")

    def withdraw(self):
        amt= float(input("enter withdrawal amount:"))
        if 0<amt<=self.balance:
            self.balance-=amt
            print("withdrawn:",amt)
        else:
            print("insufficient balance")

    def display(self):
        print("\naccount no:",self.acc_no)
        print("name:",self.name)
        print("type:",self.acc_type)
        print("balance:",self.balance)

acc = bankaccount(101, "sree", "savings", 5000)
acc.display()
acc.deposit()
acc.withdraw()
acc.display()