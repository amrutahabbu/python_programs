'''(The Account class) Design a class named Account that contains:'''
import math
from _ast import mod, Return


class RegularPolygon:
    def __init__(self,n = 3,side = 1 , x = 0 ,y =0):  #like Constructor in java
        self.__n = n #attribute
        self.__side = side #attribute
        self.__x = x
        self.__y = y

    def get_n(self):
        return self.__n
    def get_side(self):
        return self.__side
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def set_n(self,n):
         self.__n = n
    def set_side(self,side):
         self.__side = side
    def set_x(self,x):
         self.__x = x
    def set_y(self,y):
         self.__y = y


    def getPerimeter(self):
        perimeter = 0
        for i in range(1,self.get_n()+1):
            perimeter += self.get_side()
        return perimeter

    def getArea(self):
        area =0
        PI = 3.14

        area= ((self.get_n()) * self.get_side()**2) / (4 * ( math.tan( PI / self.get_n())))

        return area



triangle = RegularPolygon()
hexagon = RegularPolygon(6,4)
reg =  RegularPolygon(10, 4, 5.6, 7.8)

print("Perimeter is : ",triangle.getPerimeter())
print("Perimeter is : ",hexagon.getPerimeter())
print("Perimeter is : ",reg.getPerimeter())

print("Area is : ",triangle.getArea())
print("Area is : ",hexagon.getArea())
print("Area is : ",reg.getArea())

