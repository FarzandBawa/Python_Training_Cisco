l1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
for i, v in enumerate(l1):
    l1[i] = v * v
print(l1)
l2 = [v * v for v in l1]
print(l2)
l2 = [v for v in l1 if v % 2 != 0]
print(l2)

l2 = [v if v % 2 != 0 else v * v for v in l1]
print(l2)
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = []
for value in l1:
    l2.extend(value)
print(l2)

l2 = [value1 for value in l1 for value1 in value]
print(l2)
l3 = [l2.extend(v) for v in l1]
print(l2)
l2 = [v[0] for v in l1]
print(l2)

l = [1, 2, 3, 4]
for i, v in enumerate(l):
    print("i", i, "v", v)

Map, Lambda, Filter


def sq(n):
    n += 1
    return n * n


l2 = list(map(sq, l1))
print(l2)

Lambda
l2 = list(map(lambda n: n * n, l1))
print(l2)

Filter
l2 = list(filter(lambda n: (n % 2 != 0), l1))
print(l2)
