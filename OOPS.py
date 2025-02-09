class BankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def withdraw(self,amt):
        if self.balance<amt:
            print("Insufficient balance")
        else:
            self.balance-=amt
            print(f"{self.balance} is your current account balance")

    def deposit(self,amt):
        self.balance+=amt
        print(f"{amt} was deposited! {self.balance} is your current account balance")

    def __repr__(self):
        return f"Name:{self.owner}\nBalance:{self.balance}"

acct1= BankAccount("Jose",100)
print(acct1)
acct1.owner
acct1.balance
acct1.withdraw(50)
acct1.deposit(75)
acct1.withdraw(500)