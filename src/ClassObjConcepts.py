# We can create the class using Class keyword

class myfirstClass:
    print("Hello Class")
#Object Creation of myfirst Class
p1=myfirstClass()
print(p1)

"""The __init__() Function

The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

class persondetails:
    def __init__(self,name):
        self.name=name

p2=persondetails("Akshay")
print(p2.name)

"""Note: The __init__() function is called automatically every time the class is being used to create a new object."""

class defaultcalss:
    def __init__(self):
        print("Default class")

p3=defaultcalss()
print(p3)

"""Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object."""

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunction(self):
        print(self.name)

c=person('Akshay',25)
c.myfunction()
"""Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""
class cardetails:
    def __init__(mypersonalsf,carname,carno):
        mypersonalsf.carname=carname
        mypersonalsf.carno=carno
car=cardetails("BWM",565454)
print(car.carname,car.carno)
#Modify Object Properties
car.carname="SNDRO"
print(car.carname,car.carno)

# We can delete the properties of object or object using del method

"""del car.carname
print(car.carname,car.carno)
"""
"""
del car
print(car.carname,car.carno)
"""