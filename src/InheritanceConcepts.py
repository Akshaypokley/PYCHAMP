class Person:
    def __init__(self,FirstName,LastName):
        self.FirstName=FirstName
        self.LastName=LastName

    def StName(self):
        print(self.LastName,self.FirstName)


class StudClss(Person):
    pass
s=StudClss("Akshay","Pokley")
s.StName()
#Instead of pass we also used init function into chield class

class  stinit(Person):
    def __init__(self,Sname,Slname):
        Person.__init__(self,Sname,Slname)

ss=stinit("Rajesh"," Karamore")
ss.StName()

class CarDetails:
    def __init__(self,CarModelName):
        self.CarModelName=CarModelName
    def PrintCard(self):
        print(self.CarModelName)
class CarChild(CarDetails):
     def __init__(self,CarMoDN,CarName):
         super().__init__(CarMoDN)
         self.CarModelN=CarName

c=CarChild("420",'BMW')
print(c.CarModelN)

"""By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent."""