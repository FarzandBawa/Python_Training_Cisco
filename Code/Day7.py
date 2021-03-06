# oops:-
#
# empid,sal,name,mail
# class method
# static method


class emp:
    a = 10

    @classmethod
    def incra(cls):
        cls.a += 1

    @staticmethod
    def incra2():
        print(a)

    def __init__(self, empid, sal, name, mail):
        self.__empid = empid
        self.__sal = sal
        self.__name = name
        self.__mail = mail
        emp.incra()

    def incrSal(self):
        self.__sal += (self.__sal * .1)
        return self.getSal()

    def getSal(self):
        return self.__sal


empobj1 = emp(123, 2000, "ABC", "mail@tc")
empobj2 = emp(234, 3000, "PQR", "mail@tcs")

print(empobj2.incrSal())
empobj2.incra()
print(empobj2.a)
# empobj1.a = 20
# print(emp.a)
# print(empobj1.a)
