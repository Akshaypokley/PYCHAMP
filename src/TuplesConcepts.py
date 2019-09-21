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

