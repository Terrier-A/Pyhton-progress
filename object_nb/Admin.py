from User import User


class Admin(User):

    def __init__(self, firstname, lastname, rights):
        User.__init__(self, firstname, lastname)
        self.rights = rights

    @property
    def rights(self):
        return self.__rights

    @rights.setter
    def rights(self, rights):
        if not isinstance(rights, str):
            raise BaseException("rights must be a string")
        rights = rights.strip()
        if rights == "":
            raise BaseException("rights can't be empty")
        self.__rights = rights.lower()

    def __str__(self):
        return "%s %6s" % (User.__str__(self), self.__rights)
