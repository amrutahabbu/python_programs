'''
(Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g., 1 billion), and displays the number of years and days for
the minutes. For simplicity, assume a year has 365 days. Here is a sample run:

Enter the number of minutes:
1000000000 minutes is approximately 1902 years and 214 days
'''

user_input_minutes = eval(input("Enter the minutes"))
a_year_in_minutes = 365 * 24 *60

total_years = user_input_minutes // a_year_in_minutes
days = (user_input_minutes % a_year_in_minutes) // (24*60)

print(str(user_input_minutes) + " minutes is approximately" + str(total_years) + " years and " + str(days))

'''
  1 year = (365 * 24 * 60) minutes
  x years = user input minutes
  
  
  1 day = 24 * 60 minutes
  x days =( calculated minutes)
 '''