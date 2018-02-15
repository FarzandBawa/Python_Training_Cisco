# inheritence


class emp:

    def __init__(self, empid, sal, name, mail):
        self.__empid = empid
        self.__sal = sal
        self.__name = name
        self.__mail = mail

    def incrSal(self):
        self.__sal += (self.__sal * .1)
        return self.getSal()

    def getSal(self):
        return self.__sal


class developer(emp):
    def __init__(self, empid, sal, name, mail, lang):
        super().__init__(empid, sal, name, mail)
        self.__lang = lang


devobj1 = developer(132, 2000, "Hashmi", "abs@gmail.com", "Python")

# print(devobj1.getSal())
print(help(developer))
