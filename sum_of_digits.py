'''(Sum the digits in an integer) Write a function that computes the sum of the digits
in an integer. Use the following function header:
def sumDigits(n):
For example, sumDigits(234) returns 9 (Hint: Use the % operator
to extract digits, and the // operator to remove the extracted digit. For instance, to
extract 4 from 234, use 234 % 10 To remove 4 from 234, use 234 // 10
Use a loop to repeatedly extract and remove the digits until all the digits
are extracted.) Write a test program that prompts the user to enter an integer and
displays the sum of all its digits.'''


# Function to calculate the sum of digits
def sumDigits(number):

    sum = 0

    while number > 0:

        digit = number % 10
        sum += digit
        number //= 10

    return sum

# Input a number from the user
num = eval(input("Enter a number: "))


result = sumDigits(num)
print("Sum of digits:", result)