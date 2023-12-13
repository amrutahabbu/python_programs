import math


class Point:
    def __init__(self, x = 0 ,y =0):  #like Constructor in java

        self.__x = x
        self.__y = y


    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y


    def set_x(self,x):
         self.__x = x
    def set_y(self,y):
         self.__y = y


    def distance(self,p2):

        xDistance = p2.__x - self.__x
        yDistance = p2.__y - self.__y
        dist = math.sqrt(xDistance ** 2 + yDistance ** 2)
        return dist

    def isNearby(self,dist):
     if(dist < 5):
      print("The two points are near")
     else:
      print("points are not  near")



x1,y1,x2,y2 = eval(input("enter x1,y1,x2,y2"))

p1 = Point(x1,y1)
p2= Point(x2,y2)

dist = p1.distance(p2)
print("The distance between two points is ",dist)
p1.isNearby(dist)