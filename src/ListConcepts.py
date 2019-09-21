""""List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members."""

list1=['A','B','A',98,8,88,88,5]
print(list1)

#Accessing item based on index value

print(list1[5])#--Positive indexing
print(list1[-5])#--Negative Indexing
print(list1[3:8])#-- +ve Ranging
print(list1[-5:-2])#-- +ve Ranging

#Change Item value
list1[6]=100
print(list1)

#Methods in list

#len
print(len(list1))

#Append
list1.append(545)
print(list1)

#insert
list1.insert(4,"AKS")
print(list1)

#Remove Delete
list1.remove("AKS")
print(list1)
del list1[5]
print(list1)

#pop
print(list1.pop())

"""#Clear
list.clear()
print(list())
"""
#copy
mylist=list1.copy()
print(mylist)
#another Method to copy the list using List fuction
ls2=['A','B','A']
my=list(ls2)
print(my)

#joine list
print(list1+ls2)

#List Constructor
Thisl=list((5,8,36,1,87,7))
print(Thisl)

"""List Methods

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""