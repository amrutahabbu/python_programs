'''(The Account class) Design a class named Account that contains:'''
import math
from _ast import mod, Return


class Linearequation:
    def __init__(self,a,b,c,d,e,f):  #like Constructor in java
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f


    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def get_d(self):
        return self.__d
    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f


    def set_a(self,a):
         self.__a = a
    def set_b(self,b):
         self.__b = b
    def set_c(self, c):
        self.__c = c
    def set_d(self, d):
        self.__d = d
    def set_e(self, e):
        self.__e = e
    def set_f(self, f):
        self.__f = f

    def  isSolvable(self):

        denominator = (self.get_a() *self.get_d()) - (self.get_b() *self.get_c())
        return denominator


    def getX(self,deno):


            x = (self.get_e() * self.get_d() - self.get_b() * self.get_f()) / deno
            return x


    def getY(self,deno):


            y = (self.get_a() * self.get_f() - self.get_e() * self.get_c()) / deno
            return y



l = Linearequation(3,4,3,8,2,4)
solvableAnswer = l.isSolvable()
if solvableAnswer  != 0:
    print(l.getX(solvableAnswer))
    print(l.getY(solvableAnswer))
else:
    print ("Non Solvable Equation")