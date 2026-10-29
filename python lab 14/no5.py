class Rational:
    def __init__(self, numerator=0, denominator=1):
        try:
            divisor = self.gcd(numerator, denominator)
            if divisor == 0:
                raise ZeroDivisionError
            self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
            self.__denominator = int(abs(denominator) / divisor)
        except ZeroDivisionError:
            raise ZeroDivisionError("Error in the constructor of class Rational!")

    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __getitem__(self, index):
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator

    def gcd(self, n, d):
        if d == 0:
            return n
        else:
            return self.gcd(d, n % d)


def rationalTest(numer1, denom1, numer2, denom2):
    try:
        rat1 = Rational(numer1, denom1)
        rat2 = Rational(numer2, denom2)
        print(rat1, "+", rat2, "=", rat1 + rat2)
    except ZeroDivisionError:
        print("A ZeroDivisionError is encountered in the constructor of class Rational!")


rationalTest(1, 3, 2 ,5)
rationalTest(2, 0)
