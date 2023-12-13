'''
(Compute the greatest common divisor) For Listing 5.8, another solution to find
the greatest common divisor of two integers n1 and n2 is as follows: First find d to
be the minimum of n1 and n2, and then check whether d, d - 1, d - 2, ..., 2, or
1 is a divisor for both n1 and n2 in this order. The first such common divisor is the
greatest common divisor for n1 and n2.
'''


'''
Calculated GCD in two ways
'''

gcd = 1
num1 = 10
num2 = 32

for i in range(2,min(num1,num2),1):
    if num1 % i ==0 and num2 % i ==0:
        gcd = i


print("GCD is " , gcd)

for i in range(min(num1,num2),1,-1):
    if num1 % i ==0 and num2 % i ==0:
        gcd = i
    break
print("GCD is " , gcd)