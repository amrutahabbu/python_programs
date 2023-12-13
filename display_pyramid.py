'''
(Display a pyramid) Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid, as shown in the following sample run:

'''

input_user_rows = eval(input("Enter an integer from 1 to 15: "))


# Display the pyramid
for i in range(1, input_user_rows + 1):
    # Print spaces before the asterisks
    spaces = " " * (input_user_rows - i)
    # Print asterisks
    asterisks = str(i) * (2 * i - 1)
    print(spaces + asterisks)


# Display the pyramid
for i in range(1, input_user_rows + 1):
    # Print spaces before the asterisks
    spaces = " " * (input_user_rows - i)
    # Print asterisks
    asterisks = str(i) * (2 * i - 1)
    print(spaces + asterisks)





