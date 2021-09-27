class User(object):
    def __init__(self, fisrtname, lastname):
        self.lastname = lastname
        self.firstname = fisrtname

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        if not isinstance(firstname, str):
            raise BaseException("firstName must be a string")
        firstname = firstname.strip()
        if firstname == "":
            raise BaseException("firstName can't be empty")
        firstname = firstname.lower()
        self.__firstname = firstname.capitalize()

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        if not isinstance(lastname, str):
            raise BaseException("lastName must be a string")
        lastname = lastname.strip()
        if lastname == "":
            raise BaseException("lastName can't be empty")
        self.__lastname = lastname.upper()

    def __str__(self):
        return "%15s %15s" % (self.__firstname, self.__lastname)
