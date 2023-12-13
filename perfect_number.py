'''(Perfect number) A positive integer is called a perfect number if it is equal to the
sum of all of its positive divisors, excluding itself. For example, 6 is the first perfect number, because The next is
There are four perfect numbers less than 10,000. Write a program to find these
four numbers.'''


def is_perfect_number(number):
    sum = 0
    for i in range(1,number):

        if number % i == 0:
            sum = sum + i

    if(sum == number):
        return True
    else:
        return False

print(is_perfect_number(6))

list_of_perfect_numbers =[]

for i in range (2,10001):
    answer = is_perfect_number(i)
    if(answer):
        list_of_perfect_numbers.append(i)

for i in list_of_perfect_numbers:
 print(i)

