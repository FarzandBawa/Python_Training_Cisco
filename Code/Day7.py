# oops:-
#
# empid,sal,name,mail


class emp:
    a = 10

    def __init__(self, empid, sal, name, mail):
        self.__empid = empid
        self.__sal = sal
        self.__name = name
        self.__mail = mail

    def incrSal(Z:
        self.__sal += (self.__sal * .1)
        return self.getSal()

    def getSal(self):
        return self.__sal


empobj1 = emp(123, 2000, "ABC", "mail@tc")
empobj2 = emp(234, 3000, "PQR", "mail@tcs")

print(empobj2.incrSal())
print(emp.a)
