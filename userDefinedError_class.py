class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):

        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        raise RuntimeError("These sides do not form a triangle")

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3




class Triangle(TriangleError):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        if self.is_valid_triangle(side1,side2,side3):
         self.__side1 = side1
         self.__side2 = side2
         self.__side3 = side3
         print("Triangle is created")
        else:
         raise TriangleError(side1, side2, side3)


    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def is_valid_triangle(self, side1, side2, side3):
        return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1



s1,s2,s3 = eval(input("Enter the sides"))
t= Triangle(s1,s2,s3)
