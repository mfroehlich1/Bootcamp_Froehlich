# Let's represent an ATM with a class containing a balance property. A newly
# created account will default to a balance of 0. Implement the initializer,
# as well as the following methods:
#
# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it

# Have the ATM maintain a list of transactions. Every time the user makes a deposit
# or withdrawal, add a string to a list saying 'user deposited $15' or
# 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

# > what would you like to do (deposit, withdraw, check balance, history)?
# > deposit
# > how much would you like to deposit?
# > $5
# > what would you like to do (deposit, withdraw, check balance, history)?
# > check balance
# > balance: $5

class CheckingAccount:
    def __init__(self):
        self.transactions = []
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited: ${amount}')

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f'User withdrew: ${amount}')

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)


bankaccount = CheckingAccount()

while True:
    print('\nChoose to (deposit), (withdraw), (check balance), (list transactions), or (exit)\n')
    choice = input('Choice: ')
    amount = 0

    if choice == 'deposit':
        amount = int(input('Amount: '))
        bankaccount.deposit(amount)

    elif choice == 'withdraw':
        amount = int(input('Amount: '))
        bankaccount.withdraw(amount)

    elif choice == 'check balance':
        balance = bankaccount.check_balance()
        print(f'Balance: {balance}')

    elif choice == 'list transactions':
        bankaccount.print_transactions()

    elif choice == 'exit':
        break

    else:
        print('Please input a valid command.')
        continue
