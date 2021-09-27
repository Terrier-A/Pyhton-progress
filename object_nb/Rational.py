class Rational(object):
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den
        self.simplify()

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise BaseException("Un numérateur doit être un entier")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise BaseException("Un dénominateur doit être un entier)")
        if value == 0:
            raise BaseException("Un denominateur ne peut être nul (toi si!)")
        else:
            self.__denominator = value

    def simplify(self):
        divisor = 2
        while divisor <= min(self.__numerator, self.__denominator):
            while self.__numerator % divisor == 0 and self.__denominator % divisor == 0:
                self.__denominator /= divisor
                self.__numerator /= divisor
            divisor += 1

    def __str__(self):
        return "[%d/%d]" % (self.__numerator, self.__denominator)

    def __add__(self, r2):
        return Rational(self.numerator * r2.denominator + self.denominator * r2.numerator,
                        self.denominator * r2.denominator)
