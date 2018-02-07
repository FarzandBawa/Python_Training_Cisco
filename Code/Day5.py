def add(a, b, c):  # default argument
    print(a)
    return a + b + c


# print(add(10,20)) # positional arguments
print(add(c=10, b=10, a=40))  # keyword arguments

# wap count vowels and consonants from the str


def vcCount(s):
    v = c = 0
    for i in s:
        if i in 'aeiou':
            v += 1
        elif i != ' ':
            c += 1
    return v, c


s = "Python String"  #
v, c = vcCount(s)
print("Vowel", v)
print("consonant", c)

#packing and unpacking


def add(*l):
    return sum(l)


print(add(10, 20, 30, 40, 50, 340))


def add(a, b, c, d):
    return sum(l)


l = [10, 20, 30, 40]
print(add(*l))

# using dict:- 
d = {'a': 10, 'b': 20, 'c': 30}

def printVal(a, b, c):
    print(a, b, c)

def printD(d):
    print(d)

printD(d) # to pass etire dict
printVal(*d) # to get keys
printVal(**d) # to get values but works same as keyword args so the receiving args have to match the dict keys


