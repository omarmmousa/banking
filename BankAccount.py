#!/usr/bin/python
# ||===========================================||
# ||      Bank Account class definition        ||
# ||===========================================||
class BankAccount():
    # initializing the class
    def __init__(self, initial_balance = 0.00):
        self.balance = initial_balance
    # deposit function (allows user to deposit money in account)
#    def deposit(self, amount):
#         self.balance += amount
#         return self.balance
# withdraw function (allows user to withdraw from account)
    def withdraw(self, amount):
         self.balance -= amount
         return self.balance
# spending function (allows user to input how much they want to spend)
#    def spend(self, amount):
#        self.balance -= amount
# overdraw function (determine if the account is overdrawn)
#    def overdrawn(self):
#        return self.balance < 0



# ||===========================================||
# ||             Main Function                 ||
# ||===========================================||
#my_account = BankAccount(10.94)

# user input of their current balance
currentBalance = input('Enter your current Balance:')
# initializing the bank account with the courrent balance
my_account = BankAccount(currentBalance)
if float(my_account.balance) > 0.00:
    print(' OPTIONS:\n' '1. Check Balance \n' '2. Deposit \n' '3. Withdraw \n' '4. Spend \n')
    choice = input("what is your choice from the above options: ")
    print("you chose OPTION #: ", choice)
    if choice is '1':
        print("You have: $",my_account.balance,"in your bank Account")
#    elif choice is '2':
#        newBalance = input("How much are you depositing today?: ")
#        print("You're depositing $: ", newBalance, "into your account")
#        my_account.deposit(newBalance)
#        print(my_account.balance)
    elif choice is '3':
            draw = input("how much are your withdrawing")
            print("You want to withdraw: $", draw)
            my_account.withdraw(draw)
            print("now you are left with: $", float(my_account.balance))



    #    print("You now have: $",my_account.balance,"in your bank Account")
#stackChips = input("How much are you deposting in your bank account:")
#my_account.deposit(stackChips)
#print("New Balance is: $", my_account.balance)
