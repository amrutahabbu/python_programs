'''
(Science: day of the week) Zeller’s congruence is an algorithm developed by
Christian Zeller to calculate the day of the week. The formula is
where
■ h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday,
4: Wednesday, 5: Thursday, 6: Friday).
■ q is the day of the month.
■ m is the month (3: March, 4: April, ..., 12: December). January and February are
counted as months 13 and 14 of the previous year.
■ j is the century (i.e., ).
■ k is the year of the century (i.e., year % 100).
Write a program that prompts the user to enter a year, month, and day of the
month, and then it displays the name of the day of the week. Here are some sample runs


Enter year: (e.g., 2008):
Enter month: 1-12:
Enter the day of the month: 1-31:
Day of the week is Friday
'''

def zellers_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    K = year % 100
    J = year // 100

    h = (day + (13 * (month + 1) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7


    days_of_week = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }

    return days_of_week[h]

# Input date (day, month, year)
day = int(input("Enter day : "))
month = int(input("Enter month : "))
year = int(input("Enter year :  "))

day_of_week = zellers_congruence(day, month, year)
print(f"The day of the week is" ,day_of_week)
