'''(Sum a series) Write a program to sum the following series:'''

sum = 0
numerator = 1
denominator = 99

for i in range (numerator,denominator-1,2):

    sum += (i/(i+2))

print(sum)
