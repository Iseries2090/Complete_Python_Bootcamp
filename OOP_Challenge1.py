"""
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals,
and test to make sure the account can't be overdrawn.
"""


class Account:
    def __init__(self,name,balance):
        self.owner = name
        self.balance = balance
    
    def deposit(self,num):
        self.balance = self.balance + num
        print('Deposit {} to your account.  New balance is {}.'.format(num,self.balance))
    
    def withdraw(self,num):
        if num > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance = self.balance - num
            print('Withdrawed {} amount from your total balance {}'.format(num,self.balance))
        
    def __str__(self):
        return f"Account owner: {self.owner} \nAccount Balance: {self.balance}"

#1. Instantiate the class
acct1 = Account('Jose',100)

#2 Print the object
print(acct1)

#3 show the account owner attribute
print(acct1.owner)

#4 Show the account balance attribute
print(acct1.balance)

#5 Make a series of deposits and whithdrawals
acct1.deposit(50)
acct1.withdraw(75)

#6 Make a withdrawal that exceeds the available balance
acct1.withdraw(500)