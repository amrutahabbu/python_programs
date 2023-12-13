'''
(Sum the digits in an integer) Write a program that reads an integer between 0 and
1000 and adds all the digits in the integer. For example, if an integer is 932, the
sum of all its digits is 14. (Hint: Use the % operator to extract digits, and use the //
operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 //
10 = 93.) Here is a sample run:
'''

num = eval(input("Enter a number between 0 to 999"))
sum_of_digits = 0
for i in range(0,3):
 if(num > 999 or num < 0):
  print("Invalid number")
 else :
  digit = num % 10
  num = num // 10
  sum_of_digits = sum_of_digits + digit

print(sum_of_digits)
