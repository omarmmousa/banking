#!/usr/bin/python
# ||===========================================||
# ||      Bank Account class definition        ||
# ||===========================================||
class BankAccount():
    # initializing the class
    def __init__(self, initial_balance = 0.00):
        self.balance = initial_balance
    # deposit function (allows user to deposit money in account)
    def deposit(self, amount):
        self.balance += amount
# withdraw function (allows user to withdraw from account)
    def withdraw(self, amount):
         self.balance -= amount
# spending function (allows user to input how much they want to spend)
    def spend(self, amount):
        self.balance -= amount
# overdraw function (determine if the account is overdrawn)
    def overdrawn(self):
        return self.balance < 0
# ||===========================================||
# ||             Main Function                 ||
# ||===========================================||
# user input of their current balance
currentBalance = float(input('Enter your current Balance:'))
# initializing the bank account with the courrent balance
my_account = BankAccount(currentBalance)

if float(my_account.balance) > 0.00:
    print(' OPTIONS:\n' '1. Check Balance \n' '2. Deposit \n' '3. Withdraw \n' '4. Spend \n')
    choice = input("what is your choice from the above options: ")
    print("you chose OPTION #: ", choice)

    if choice is '1':
        print("You have: $",my_account.balance,"in your bank Account")

    elif choice is '2':
        newBalance = float(input("How much are you depositing today?: "))
        my_account.deposit(newBalance)
        print(my_account.balance)

    elif choice is '3':
            draw = float(input("how much are your withdrawing $: "))
            my_account.withdraw(draw)
            if my_account.balance < 0:
                my_account.overdrawn()
                print("You are overdrawn and now your sitting on $: ", my_account.balance)
            else:
                print("You now have :$ ", my_account.balance)


    elif choice is '4':
        spendMoney = float(input("How much do you want to spend $: "))
        my_account.spend(spendMoney)
        if my_account.balance < 100.00:
            print("Sorry buddy can't buy that")
        else:
            print("You have: $", my_account.balance)
