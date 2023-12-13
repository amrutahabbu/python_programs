'''(Financial application: compound value) Suppose you save $100 each month into
a savings account with an annual interest rate of 5%. Therefore, the monthly interest rate is After the first month, the value in the account
becomes
100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
(100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
(100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month. Here is a sample run of the
program:

Enter the monthly saving amount: 100
After the sixth month, the account value is 608.81


'''

monthly_saving_amount = eval(input("Enter the monthly saving amount"))
annual_interest_rate = eval(input("Enter the interest rate"))

monthly_interest_rate = (annual_interest_rate / 100 )/12

r = 1+monthly_interest_rate

new_amount = 0
for i in range (0,6):
   new_amount = (new_amount + monthly_saving_amount) * r

print(round(new_amount,2))

