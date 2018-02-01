a = 1
print(str(a) + "= a") #does't throw an error but a+"=a" will throw an error
print(a,"=a")#does't throw an error

#For loop example with range() and custom step:-
for i in range(5, -5, -2):
    print(i)


#For loop using list:-
i = [10, 20, 30, 40]
for j in i:
    if j in [10, 20]:
        print(j)

# If-Elif-Else example:-        
i = 3
if i == 0:
    print("Yes")
elif i == 1:
    print("No")
else:
    print("Nothing")

## Prime Number:-
n = 5
for i in range(2, n // 2):
    if n % i == 0:
        print("Not Prime")
        break
else:
    if (n == 1) or (n == 4):
        print("Not Prime")
    else:
        print("Prime")
