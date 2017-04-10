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
