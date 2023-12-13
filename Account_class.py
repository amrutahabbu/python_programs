'''(The Account class) Design a class named Account that contains:'''


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


accounts = []
for i in range(0,10):
    accountnew = Account(i,100,4.5)
    accounts.append(accountnew)


incorrectId = True
input_Id = eval(input("Enter Account Id"))
while incorrectId == True:
 for i in range(0,10):
    account = accounts[i]
    if(account.get_id() == input_Id):
        incorrectId = False
 if incorrectId == True:
     input_Id = eval(input("Enter Account Id"))


print("Main Menu")
print("1: Check balance")
print("2: Withdraw")
print("3: Deposit")
print("4: Exit")
option = eval(input("Enter the choice"))

if(option == 1):
    print("The balance is " , accounts[input_Id].get_balance())
if(option == 2):
    print("Withdrawing $10" ,accounts[input_Id].withdraw(10))
if(option == 3):
    print("Depositing $100" , accounts[input_Id].deposit(100))
if(option == 4):
    print("Exiting")

