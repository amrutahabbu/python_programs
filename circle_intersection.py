'''
(Geometry: two circles) Write a program that prompts the user to enter the center
coordinates and radii of two circles and determines whether the second circle is
inside the first or overlaps with the first, as shown in Figure 4.11. (Hint: circle2 is
inside circle1 if the distance between the two centers <= | r1 - r2| and circle2
overlaps circle1 if the distance
'''

import math
print
x1,y1,r1,x2,y2,r2 = eval(input("Input x1, y1, r1, x2, y2, r2:"))
d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if d <= r1-r2:
    print("Circle2  is in Circle1")
elif d <= r2-r1:
    print("Circle1  is in Circle2")
elif d < r1+r2:
    print("Circumference of Circle1  and Circle2  intersect")
elif d == r1+r2:
    print("Circumference of Circle1 and Circle2 will touch")
else:
    print("Circle1 and Circle2  do not overlap")