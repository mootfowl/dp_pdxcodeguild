'''

LAB31 - ATM v1

Let's represent an ATM with a class containing two attributes: a balance and an interest rate.
A newly created account will default to a balance of 0 and an interest rate of 0.1%.
Implement the initializer, as well as the following functions:

* check_balance() returns the account balance
* deposit(amount) deposits the given amount in the account
* check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
* withdraw(amount) withdraws the amount from the account and returns it
* calc_interest() returns the amount of interest calculated on the account

'''

class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        print(f"Your balance is ${self.balance}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been added to account {self}")
        self.check_balance()

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0: # or: return self.balance - amount >= 0
            return True
        else:
            print(f"Insufficient Funds - Requested Amount: ${amount} | Current Balance: ${self.balance}")


    def withdraw(self, amount):
        confirmation = self.check_withdrawal(amount)
        if confirmation == True:
            self.balance -= amount
            print(f"${amount} has been deducted from your account.")
            self.check_balance()

    def calc_interest(self):
        interest = str(round(self.interest_rate * self.balance, 3))
        print(f"The amount of interest you can earn on your current balance is ${interest}.")


account_A = ATM()
# print(account.balance, account.interest_rate)
# print(account.check_balance())

account_A.deposit(10)
account_A.deposit(5)
account_A.withdraw(20)
account_A.withdraw(9)
print(account_A.calc_interest())

