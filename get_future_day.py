import calendar

from Assignments.myLib import get_future_day

# Prompt the user for the year and first day of the year
year = int(input("Enter the year "))
first_day_index = eval(input("Enter the first day of the year:  "))

# Create a list of month names
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def getMonth(number):
    if number == 1:
        return 'January'
    if number == 2:
        return 'February'
    if number == 3:
        return 'March'
    if number == 4:
        return 'April'
    if number == 5:
        return 'May'
    if number == 6:
        return 'June'
    if number == 7:
        return 'July'
    if number == 8:
        return 'August'
    if number == 9:
        return 'September'
    if number == 10:
        return 'October'
    if number == 11:
        return 'November'
    if number == 12:
        return 'December'
# Loop through each month and display the first day of the month
for i in range(0,12):
    # Get the number of days in the current month and year

    num_days = calendar.monthrange(year, i + 1)[1]

    # Print the month name and the first day of the month
    month = getMonth(i+1)
    print(f"{month} {year}: ")
    print(get_future_day(first_day_index))

    # Calculate the index of the first day of the next month
    first_day_index = (first_day_index + num_days) % 7