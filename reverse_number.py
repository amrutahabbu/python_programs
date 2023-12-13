'''

(Reverse number) Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order.
'''

num1 = eval(input("Enter a four digit number"))

digit1 = num1 % 10
num1 = num1 // 10

digit2 = num1 % 10
num1 = num1 // 10

digit3 = num1 % 10
num1 = num1 // 10

digit4 = num1 % 10

reversed_number = 1000*digit1 + 100*digit2 + 10 *digit3 + digit4

print("reversed number is  :  " , reversed_number)
