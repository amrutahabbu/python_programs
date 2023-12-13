'''
(Algebra: solve linear equations) You can use Cramer’s rule to solve the
following system of linear equation:

Write a program that prompts the user to enter a, b, c, d, e, and f and display the
result. If ad – bc is 0, report that The equation has no solution.

ax+by = e
cx + dy = f


'''

a,b,c,d,e,f = eval (input("Enter the values for a,b,c,d,e,f "))

denominator = (a*d - b*c)
if denominator != 0:
    x = (e*d - b*f)/denominator
    y = (a*f - e*c)/denominator
    print("x : " ,x)
    print("y : " ,y)
else:
    print("This equation has no solution")