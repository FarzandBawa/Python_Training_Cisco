# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) ##### Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5
l = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple but can be list also
e = o = 0  # mutliple variable declartion also can be e,o=0,0
for i in l:
    if i & 1:  # bitwise & 1 of any number becomes 0 for even and 1 for odd
        o += 1
    else:
        e += 1
print("Number of even numbers :", e)
print("Number of odd numbers :", o)

print("-------")

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected Output : 0 1 2 4 5
for i in range(6):
    if i != 3:
        print(i, end=' ')
print()
print("-------")

# Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0,1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 1 2 3 5 8 13 21 34
a, b = 0, 1
while a < 50:
    print(a, end=" ")
    a, b = b, a + b
print()
print("-------")

# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence

for i in range(200, 289):
    if ((i % 10) % 2 == 0 and (i // 10) % 2 == 0):
        print(i, end=",")
print(400)
print("-------")

# Write a Python program to construct the following pattern, using a nested loop number.
# 1 22 333 4444 55555 666666 7777777 88888888 999999999
for i in range(1, 10):
    for j in range(i):
        print(i, end='')
    print(end=' ')
