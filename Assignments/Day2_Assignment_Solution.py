# 1.Write a Python program to find the second smallest number in a list

l = [100, 20, 30, 4]
print(sorted(l)[1])
print("------------")

# 2. Write a Python program to convert a list of multiple integers into a single integer

l = [1, 2, 3, 4, 5]
for i in l:
    print(int(i), end='')
print()
print("------------")

# 3.Write a Python program to check a list is empty or not

l = []
if l == []:
    print("Empty list")
else:
    print("Not Empty")
print("------------")


# 4.Write a Python program to compute the differeces between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

l1, l2 = ["red", "orange", "blue", "white", "green"], ["black", "yellow", "green", "blue"]
x, y = [], []
for i in l1:
    if i not in l2:
        x.append(i)
for i in l2:
    if i not in l1:
        y.append(i)
print("Color1-Color2 :", x)
print("Color2-Color1 :", y)
print("------------")


# 5.Write a Python program to count the number of characters (character frequency) in a string
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s, d = "google.com", {}
for i in s:
    if d.get(i) == None:
        d[i] = s.count(i)
print(d)
print("------------")


# 6.Write a Python program that takes a list of words and returns the length of the longest one

l, length = ["Python", "program", "write", "a", "returns", "length"], 0
for i in l:
    if length < len(i):
        length = len(i)
print(length)
print("------------")

# 7.Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

s = "Please enter any string"
count = 0
for i in s[:4]:
    if i.isupper():
        count += 1
    if count == 2:
        print(s.upper())
        break
else:
    print(s)
