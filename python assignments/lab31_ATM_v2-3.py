'''

LAB31 - ATM v3

v2:
Have the ATM maintain a list of transactions.
Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'.
Add a new function print_transactions() to your class for printing out the list of transactions.

v3:
Allow the user to enter commands into a REPL.

'''

import time


class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []
        self.pin = '0101'
        self.pin_hint = "I am an aardvark. My name is David. I stand 32 feet tall. I have a daughter named Audrey."

    def main(self):
        print(time.strftime("%Y.%m.%d"), " | ", time.strftime("%H:%M:%S"))
        print("Welcome to Bank of David!")
        # Para continuar en espanol, marke nueve...
        while True:
            pin_attempt = input("Please enter your four digit pin, or enter 'hint'. >> ")
            if pin_attempt == self.pin:
                self.main_menu()
                return
            elif pin_attempt == 'hint':
                print(self.pin_hint)

    def main_menu(self):
        while True:
            action = input(f"Account Number: {id(self)}\nOPTIONS >> "
                           f"Balance[b] | Deposit[d] | Withdraw[w] | Interest[i] | View Transactions[v] | Exit[e] >> ")
            if action == 'b':
                self.check_balance()
            elif action == 'd':
                self.deposit()
            elif action == 'w':
                self.withdraw()
            elif action == 'i':
                self.calc_interest()
            elif action == 'v':
                self.view_transactions()
            elif action == 'e':
                reminder = input("Please remove your debit card.")
                print("Have a nice day!")
                exit()

    def check_balance(self):
        print(f"\tYour balance is ${self.balance}.")

    def deposit(self):
        amount = int(input("How much would you like to deposit? >> "))
        self.balance += amount
        print(f"\t${amount} has been added to account {id(self)}")
        self.check_balance()
        self.add_transaction(amount)

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0: # or: return self.balance - amount >= 0
            return True
        else:
            print(f"\tInsufficient Funds - Requested Amount: ${amount} | Current Balance: ${self.balance}")

    def withdraw(self):
        amount = int(input("How much would you like to withdraw? >> "))
        confirmation = self.check_withdrawal(amount)
        if confirmation == True:
            self.balance -= amount
            print(f"\t${amount} has been deducted from account {id(self)}.")
            self.check_balance()
            withdrawal = amount * -1
            self.add_transaction(withdrawal)

    def calc_interest(self):
        interest = str(round(self.interest_rate * self.balance, 3))
        print(f"\tThe amount of interest you can earn on your current balance is ${interest}.")

    def add_transaction(self, amount):
        single_transaction = []
        single_transaction.append(time.strftime(f"%Y.%m.%d"))
        single_transaction.append(time.strftime("%H:%M:%S"))
        if amount < 0:
            single_transaction.append(f"WITHDRAWAL: ${amount} BALANCE: ${self.balance}")
        else:
            single_transaction.append(f"DEPOSIT: ${amount} BALANCE: ${self.balance}")
        self.transactions.append(single_transaction)

    def view_transactions(self):
        print()
        print(f"Printing all transactions for account {id(self)}...")
        for item in self.transactions:
            print(f"\t{item}")

dp = ATM()
dp.main()

