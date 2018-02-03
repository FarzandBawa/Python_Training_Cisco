# List
l = [21, 45.67, 678, "abc"]
l.append("ghi")
print(l)
l[1] = 65
print(l)
l.append(678)
print(l)
print(len(l))
del (l[1])
print(l)
print(l[1:3])
l = [10] * 10
print(l)
l = [10, 20, 30, 4]
# l.sort()
# print(l)
sorted(l)
print(l)
# print(help(sorted))
# Numbers
# v = 90**10
# print(v)
import math
# print(dir(math))
# String
v = "565656 56465464"
print(v.split())
print(v.count('5'))
print(help(str))
s1 = ["abc", "def"]
s2 = ["ghi"]
print("".join(s1 + s2))
# print(help(str))
import random
# print(help(random))

# Dictionary

d = {"abc": 1, "def": 2}
d["ghi"] = 3
print(d)
{1: 1, 2: 4, 3: 9, 4: 16}

n = 10
d = {}
for i in range(1, n + 1):
    d[i] = i**2
print(d)
