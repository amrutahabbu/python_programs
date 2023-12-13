'''

(Geometry: area of a triangle) Write a program that prompts the user to enter the
three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
The formula for computing the area of a triangle is
Here is a sample run:

Enter three points for a triangle:
The area of the triangle is 33.6
'''

import math1

x1,y1 = eval(input("Enter x1 and y1"))
x2,y2 = eval(input("Enter x2 and y2"))
x3,y3 = eval(input("Enter x3 and y3"))

side1 = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
side2 = math.sqrt(((x3-x3)**2) + ((y3-y2)**2))
side3 = math.sqrt(((x3-x1)**2) + ((y3-y1)**2))




s = round( (side1 + side2 + side3) / 2)
print(s)
print(round(s))
area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3) )
print(area)
var1 = s-side1
var2 = s-side2
var3 = s-side3


area_1 = s * var1 * var2 * var3
area = math.sqrt(area_1)
print(" The area of the triangle is " + str((area)))