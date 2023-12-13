'''(Palindromic prime) A palindromic prime is a prime number that is also palindromic. For example, 131 is a prime and also a palindromic prime, as are 313 and
757. Write a program that displays the first 100 palindromic prime numbers. Display 10 numbers per line and align the numbers properly, as follows:
2 3 5 7 11 101 131 151 181 191
313 353 373 383 727 757 787 797 919 929'''
from Assignments.myLib import isPrimeNumber
from Assignments.myLib import isPalindromicNumber

number = 1
count = 0
while count <= 100:

    isprime = isPrimeNumber(number)
    isPalindrome = isPalindromicNumber(number)
    if(isprime and isPalindrome):
        print(number," ")
        count+=1
    number+=1




