class MyClass:
    """

    """

    def __init__(self, num, den):
        """

        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut être nul")
        self.setnumerateur(num)
        self.setdenumerateur(den)

    def getnumerateur(self):
        return self.__numerateur

    def setnumerateur(self, value):
        if not isinstance(value, int):
            raise BaseException("Un numérateur doit être un entier (ton cerveau ne l'est pas )")
        self.__numerateur = value

    def getdenumerateur(self):
        return self.__denominateur

    def setdenumerateur(self, value):
        if not isinstance(value, int):
            raise BaseException("Un dénominateur doit être un entier (ton cerveau ne l'est pas )")
        if value == 0:
            raise BaseException("Un denominateur ne peut être nul (toi si!)")
        else:
            self.__denominateur = value

    def __str__(self):
        return "[%d/%d]" % (self.__numerateur, self.__denominateur)

    def simplify(self):
        divisor = 2
        while divisor <= min(self.__numerateur, self.__denominateur):
            while self.__numerateur % divisor == 0 and self.__denominateur % divisor == 0:
                self.__denominateur /= divisor
                self.__numerateur /= divisor
            divisor += 1
