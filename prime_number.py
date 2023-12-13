'''
(Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
isPrime(number) function for testing whether a number is prime. Use this
function to find the number of prime numbers less than 10,000.
'''
from Assignments.myLib import isPrimeNumber

print("The prime numbers less than 1000 are : ")

for i in range (1 , 10000):
    isprime = isPrimeNumber(i)
    if(isprime):
        print(i)
