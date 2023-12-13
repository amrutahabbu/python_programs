'''(The Account class) Design a class named Account that contains:'''
from _ast import mod


class Account:
    def __init__(self,id = 0,balance = 100.0 , annualInterestRate = 0.0):  #like Constructor in java
        self.__id = id #attribute
        self.__balance = balance #attribute
        self.__annualInterestRate = annualInterestRate


    def get_id(self):
        return self.__id
    def get_balance(self):
        return self.__balance
    def get_annualInterestRate(self):
        return self.__annualInterestRate

    def set_id(self,id):
         self.__id = id
    def set_balance(self,balance):
         self.__balance = balance
    def set_annualInterestRate(self,interestrate):
         self.__annualInterestRate = interestrate


    def deposit(self,depositAmount):
        print("Deposit method")
        currBalance = self.get_balance()
        self.set_balance(currBalance+depositAmount)



    def withdraw(self,withdrawAmount):
        print("Deposit method")
        currBalance = self.get_balance()
        self.set_balance(currBalance - withdrawAmount)

    def getMonthlyInterest(self):
        currBalance = self.get_balance()
        annualIR = self.get_annualInterestRate() / 100
        monthlyInterest = currBalance * (annualIR / 12)
        return monthlyInterest

account1 = Account(1122,20000,4.5)
account1.withdraw(2500)
account1.deposit(3000)

print("ID" , account1.get_id())
print("Balance" , account1.get_balance())
print("MOnthly Interest " , account1.getMonthlyInterest())


