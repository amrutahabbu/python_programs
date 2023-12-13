'''
(Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
number. The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is
$10,000.
2. If all the digits in the user input match all the digits in the lottery number, the
award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is
$1,000.
'''
import random

user_number = eval(input("Enter the three digit number"))
lottery_number = random.randint(100,1000)
award = "$10000"

un_digit1 = (user_number // 100)
un_digit2 = (user_number //10) % 10
un_digit3 = (user_number) % 10

lottery_n1 = lottery_number //100
lottery_n2 = (lottery_number //10 ) % 10
lottery_n3 = lottery_number % 10

print(un_digit1 ,un_digit2 ,un_digit3 ,lottery_n1 ,lottery_n2 ,lottery_n3)



if user_number == lottery_number:
    print("Award is ",award)
elif(un_digit1 == lottery_n3 and un_digit2 == lottery_n2 and un_digit3 ==lottery_n1):
    print("Award is $3000")
elif(un_digit1 == lottery_n3  or un_digit1 == lottery_n2 or un_digit1 == lottery_n1  or
     un_digit2 == lottery_n3  or un_digit2 == lottery_n2 or un_digit2 == lottery_n1 or
     un_digit3 == lottery_n3 or un_digit3 == lottery_n2 or un_digit3 == lottery_n1):
    print("Award is $1000")