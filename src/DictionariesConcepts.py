"""Dictionary
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values."""

Dir={
    'key':'Value',
    'Num':54
}

print(Dir)

#We  can access the items of a dictionary by referring to its key name, inside square brackets or using get method

print(Dir['Num'])
print(Dir.get('Num'))

#We can change the value of a specific item by referring to its key name:
Dir['Num']=588744
print(Dir['Num'])

if 'Num' in Dir:
    print("True")

print(len(Dir))

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
Dir['Guru']=99
print(Dir)

Dir['Akshay']=85
print(Dir)

"""Remove methods in Dictor
The pop() method removes the item with the specified key name:
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
The del keyword removes the item with the specified key name:The del keyword can also delete the dictionary completely:
The clear() keyword empties the dictionary:
"""

Dir.pop('Num')
print(Dir)
#Dir.popitem()
#print(Dir)

del Dir['Akshay']
print(Dir)

#Dir.clear()
#print(Dir)

"""Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy() Another one is built-in method dict().."""


dir2=Dir.copy()
print(Dir)
Dir3=dict(Dir)
print(Dir3)

"""Nested Dictionaries
A dictionary can also contain many dictionaries, this is called nested dictionaries."""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

"""OR"""

child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily2 = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)
print(myfamily2)

#Return values
for x in myfamily2:
    print(myfamily2[x])

# if we want to return both

for x,y in myfamily2.items():
    print(x,y)


    """The dict() Constructor
It is also possible to use the dict() constructor to make a new dictionary:"""

    dirr=dict(model=45,name='BMW')
    print(dirr)

    """"Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary"""