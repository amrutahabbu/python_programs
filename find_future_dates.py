'''

(Find future dates) Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display the future day of the week. Here is a sample run:
Enter today's day: 1
Enter the number of days elapsed since today: 3
Today is Monday and the future day is Thursday
3
1

Enter today's day:0
Enter the number of days elapsed since today:
Today is Sunday and the future day is Wednesday

'''
from Assignments.myLib import get_future_day

number_today = eval(input("Enter today "))
number_elapsed_days = eval(input("Enter the number of days elapsed"))

elapsed_day = ( number_elapsed_days % 7) + number_today

today = get_future_day(number_today)
future_day = get_future_day(elapsed_day)



print("Today is  : ",today ," and future day is " , future_day)
