# modes:-
# r,r+
# w,w+
# a,a+

handle = open("test.txt", 'r')
filecontent = handle.read()
print(filecontent)
print(handle.tell())
filecontent = handle.read(10)
print(handle.tell())
print(filecontent)
filecontent = handle.read(10)
print(filecontent)
print(handle.tell())
filecontent = handle.readline()
print(filecontent)
filecontent = handle.readlines()
print(filecontent)
filecontent = handle.read()
print(type(filecontent))
handle.seek(0, 0)

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters


def calcUppLow(s):
    uc = lc = 0
    for i in s:
        if i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
    return uc, lc


s = "PytHoN StRInG"
print("upper count , lower count:", calcUppLow(s))
