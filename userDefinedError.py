class Rational:
    def __init__(self, n=0, d=1):

        self.numerator = n
        self.denominator = d

        if self.denominator == 0:
            raise RuntimeError("Denominator cannot be zero.")

        else:
            print("The rational is ",self.numerator,"/",self.denominator)



r = Rational(10,0)
