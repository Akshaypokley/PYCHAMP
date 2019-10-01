#Tuple--A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple=('Akshay',"Hi",54,8.232,8478,True,8478)

print(thistuple)
#Accessing and ranging tuples based on posity and negative using index

print(thistuple[5])
print(thistuple[-5])
print(thistuple[2:6])
print(thistuple[-6:-2])

#WE CAN CHANGE THE VALUE IN THE TUPLE
y=list(thistuple) #We need to convert tuple into list first then change the value
y[4]='POKLEY'

print(len(y))

# if we want to create the tuple with single values then we need to add ',' after value otherwise it not consider as tupper

thitupp=('aksjhay',)#its a tuple

thisapp2=('akshay')#This isn't tuple

"""Remove Items
 Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

"""
del thitupp
##print(thitupp)
"""I got below error for above line because  the tuple no longer exists
Traceback (most recent call last):
  File "E:/Akshay/SELENIUM/Projects/PYCHAMP/src/TuplesConcepts.py", line 30, in <module>
    print(thitupp)
NameError: name 'thitupp' is not defined
"""


"""We can Join Two tuple using + Oprator """

##For Ex.

tp1=(45,25,14,'f')
tp2=(47,'57f')

tp3=tp1+tp2
print(tp3)

#We Also Make tuple as a constructor

tp4=tuple(('akshay','rajesh',4,3.2,636.3,True))
print(tp4)

"""Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found"""