from BankAccount import BankAccount
# ||===========================================||
# ||             Main Function                 ||
# ||===========================================||

# user input of their current balance
currentBalance = float(input('Enter your current Balance:'))

# initializing the bank account with the courrent balance
my_account = BankAccount(currentBalance)

# if the initial balance is nonzero
if float(my_account.balance) > 0.00:

# Option for user to select what they want to do
    print(' OPTIONS:\n' '1. Check Balance \n' '2. Deposit \n' '3. Withdraw \n' '4. Spend \n')
    choice = input("what is your choice from the above options: ")
    print("you chose OPTION #: ", choice)

# User chooses to view balance
    if choice is '1':

# prints the current balance of the Account
        print("You have: $",my_account.balance,"in your bank Account")

# end the transaction or keep going
        keepGo = input("Are you done with your transaction?:\n" '1.yes\n' '2.no\n')
        if keepGo is '2':
            print(' OPTIONS:\n' '1. Check Balance \n' '2. Deposit \n' '3. Withdraw \n' '4. Spend \n')
            choice = input("what is your choice from the above options: ")
            print("you chose OPTION #: ", choice)

            if choice is '1':
                    print("You have: $",my_account.balance,"in your bank Account")

            elif choice is '2':
                newBalance = float(input("How much are you depositing today?: "))
                my_account.deposit(newBalance)
                print("Your new Balance is: $", round(my_account.balance,2))
                keepGo = input("Are you done with your transaction?:\n" '1.yes\n' '2.no\n')

                if keepGo is '2':
                    print(' OPTIONS:\n' '1. Check Balance \n' '2. Deposit \n' '3. Withdraw \n' '4. Spend \n')
                    choice = input("what is your choice from the above options: ")
                    print("you chose OPTION #: ", choice)
                    if choice is '1':
                            print("You have: $",my_account.balance,"in your bank Account")

                    elif choice is '3':
                        newBalanceWD = float(input("How much would you like to withdraw today: $"))
                        my_account.withdraw(newBalanceWD)
                        if float(my_account.balance) < 100.00:
                            print("Your Remaining Balance will be: $", my_account.balance)
                            keepGo = input("Are you sure you want to proceed?"  '\n1.yes\n' '2.no\n')
                            if keepGo is '1':
                                print("Your Balance is:", my_account.balance)
                            else:
                                my_account.balance += newBalanceWD
                                print("Smart Choice, your balance is: $",my_account.balance)
                        else:
                            print("Your Balance is: $", my_account.balance)
