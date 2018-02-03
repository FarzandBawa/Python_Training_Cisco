# String Pallindrome
s = "abbgdiugw2iuga"
if(s[::-1] == s):
    print("Pallindrome")
else:
    print("Not Pallindrome")
import math
print(math.floor(10.255))
print(math.trunc(10.255))
print(math.floor(-10.01))
print(math.trunc(-10.255))
x, y = math.modf(10.255)
print(x, int(y))
l = [0.1] * 10
print(sum(l))
print(math.fsum(l))
l = [10, 20, 30]
l2 = [50, 60, 20]
l.extend(l2)
print(l)

i = 1
if i > 0:
    pass

d = {'a': 10, 'b': 20, 'c': 30}
# for i in d:
#
s = "google.com"
d = {}
print(d.get('c', "key not present"))
for i in s:
    if d.get(i) == None:
        d[i] = s.count(i)
print(d)

d = {'a': 1}
d.setdefault('a', 10)
print(d)

l1 = [10, 20, 30]
l2 = ['a', 'b', 'c', 'd']
print(dict(zip(l1, l2)))

s = "google.com"
l1, l2 = [], []
c = 0
while c < len(s):
    if s[c] not in l1:
        l2.append(1)
        l1.append(s[c])
    else:
        d = 0
        while l1[d] != s[c]:
            d += 1
        l2[d] = l2[d] + 1
    c += 1
print(dict(zip(l1, l2)))
