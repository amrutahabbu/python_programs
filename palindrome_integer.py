'''(Palindrome integer) Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns
# 654
def reverse(number):
# Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. Write a test program that prompts the
user to enter an integer and reports whether the integer is a palindrome.'''


def reverse(number):

    num_str = str(number)
    reversed_str = num_str[::-1]

    if num_str == reversed_str:
        return True
    else:
        return False

num = eval(input("Enter a number: "))

if reverse(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
