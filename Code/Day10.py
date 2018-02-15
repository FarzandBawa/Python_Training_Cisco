# Exceptions
# 1-> System Exception
# 2-> User Defined Exception
try:
    print(1)
    a = []
    print(a)
    f = open('notexsss.txt')
    print(f)

except IndexError:
    print("Index out of bounds")
except ZeroDivisionError:
    print("You are dividing by 0")
except Exception as e:
    print(e)
else:
    print("Good Code!")
finally:
    print("Bad Code!")


# print(dir(__builtins__))

# User defined Exception:-
class lessthan10(Exception):
    pass


class greaterthan20(Exception):
    pass


def checkNum():
    n = 25
    try:
        if n < 10:
            raise lessthan10
        if n > 20:
            raise greaterthan20
    except lessthan10:
        print("Value less than 10")
    except greaterthan20:
        print("Value greater than 20")


checkNum()
