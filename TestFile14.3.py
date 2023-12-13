'''
(Population projection) The US Census Bureau projects population based on the
following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days. Hint: in Python, you
can use integer division operator // to perform division. The result is an integer. For
example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5)


'''


one_birth_seconds = 7
one_death_seconds = 13
one_immigrant_seconds = 45
current_population = 312032486

total_seconds_in_year = 365*24*60*60

total_birth_in_year = total_seconds_in_year // one_birth_seconds
total_death_in_year = total_seconds_in_year // one_death_seconds
total_immigrants_in_year = total_seconds_in_year //one_immigrant_seconds


for i in range(0,4):
    current_population =  current_population + total_birth_in_year+total_immigrants_in_year - total_death_in_year
    print("The population in " + str(i+1) + " year is " + str(current_population))
print ("The total population after 5 years would be " + str(current_population))
