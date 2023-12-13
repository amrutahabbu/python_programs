import math


class GeometricObject:
    def __init__(self, color="white",filled=False):
        self.__color = color
        self.__filled = filled


    def get_color(self):
        return self.__color

    def is_filled(self):
        return self.__filled

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, color="white" , filled = False ):
        super().__init__(color,filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def getArea(self):

        s1 = self.__side1
        s2 = self.__side2
        s3 = self.__side3

        s = (s1 + s2 + s3) / 2
        area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
        return area

    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return perimeter

    def __str__(self):
        description = "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)
        return description

# Example usage:

side1 , side2, side3 = eval(input("Enter the three sies of a triangle"))
color = input("Enter color")
filledornot = bool(input("Enter 0 for not filled"))


triangle = Triangle(side1,side2,side3,color,filledornot)
print(triangle)
print(f"Area: {triangle.getArea()}")
print(f"Perimeter: {triangle.getPerimeter()}")
print(f"Color: {triangle.get_color()}")
print(f"Filled: {triangle.is_filled()}")
