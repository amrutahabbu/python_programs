'''(Sort three numbers) Write the following function to display three numbers in
increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the
function to display them in increasing order. Here are some sample runs:
'''


def displaySortedNumbers(num1, num2, num3):

    lastnumber = max(num1,num2,num3)
    firstnumber= min(num1,num2,num3)
    middlenumber = (num1+num2+num3) -(lastnumber+firstnumber)
    print (firstnumber,middlenumber,lastnumber)


num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

displaySortedNumbers(num1,num2,num3)