d={10:'a',20:'b',30:'c',40:'d'}
print(d.keys())
print(d.values())
print(d.items())
print(d.popitem())
print(d.pop(20))
print(d)
## set -mutable
a={10,20,30}
b={30,40,50}
print(a.union(b)) # same as b.union(a)
print(a.intersection(b)) # same as b.intersection(a)
print(a.difference(b)) # not same as b.difference(a)
print(b.difference(a))
print(a.symmetric_difference(b)) # same as b.symmetric_difference(a)
# a.update(b)
# print(a)
# a.intersection_update(b)
# print(a)
a.difference_update(b)
print(a)
print(a.difference(a))
a={10,20,30}
b={30}
print(b.issubset(a))
print(b.issuperset(a))
c=list(b)
if list(b) in list(a):
	print("True")
else:
	print("False")	
a.discard(10)#delete a value
a.discard(50)
a.remove(20)
#a.remove(5) //throws an error
print(a)

l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
s={(10),(30)}
print(s)

# Functions
print("Before")

def printVal(): #<-function defination
	print("Printing inside Function")

def abc():
	pass

def add(x,y=10):
	return x+y		

printVal()	#<-function call
print("After")
print(add(20,50))


