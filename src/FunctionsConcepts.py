# we can define the function using def () key work

def myFunction():
    print("My name is khan")
myFunction()

#We can pass the paramitter through function
def myParFunction(name):
    print("My name is:"+name)
myParFunction('akshay')
myParFunction("raju")
myParFunction('neha')



##Default Paramitter

def defaultFunction(country='INDIA'):
    print("My Country Name is :"+country)

defaultFunction()
defaultFunction("UROP")
defaultFunction("USA")
defaultFunction("AUS")

#We can also pass the a list as a paramitter

def listFunction(Details):
    for x in Details:
        print(x)
DetailsList=['Akshay',85,25.325,True,False]
listFunction(DetailsList)

#Same like tuple alos
def tupleFunction(DetailsTuple):
    for y in DetailsTuple:
        print(y)
Dtuple=('Akshay','Raja',454.2,44,True,False)
tupleFunction(Dtuple)

#We can also used return statement in Function

def retunFunction(Num):
    return 8*Num
print(retunFunction(8))#64
print(retunFunction(4))#32
print(retunFunction(1))#8

"""Keyword Arguments

You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter."""

def keyvalueFunction(Car1,car3,car2):
    print(car3)

keyvalueFunction(Car1='Model 452',car2=254,car3='Model 420')

"""Arbitrary Arguments

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:"""

def Stdname(*stdN):
    print(stdN)

Stdname('KADKDK',"NDJD")

"""Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming."""

def recursionFnction(k):
    if k>0:
        result=k+recursionFnction(k-1)
        print(result)
    else:
        result=0

    return result

recursionFnction(6)