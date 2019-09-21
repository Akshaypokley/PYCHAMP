a="""This is a multi String"""

print(a)

#String As a array

a="Hello World"

print(a[4])
print(a[2:5])
print(a[5:])
print(a[:2])

#Same as negative indexing

print(a[-4])
print(a[-8:-2])
print(a[-5:])
print(a[:-2])

#Str Leng

print(len(a))

"""Now we are learn string method """

#Strip --it's used for remove the white space from string --consider below example

s=" Hello India "
print(s.strip())

#Lower and upper method

print(s.upper())
print(s.lower())

#Replace the letter in the string

print(s.replace('H','K'))

# Split
print(s.split(" "))

#Using in and not in method we can check perticular string are Available in the string

str=" I love python and java technical skills"

print('java'in str)#True
print("Ruby" in str)#False
print('ruby' not in str)#True

#String Concatenation\

str ='Hello'
str1='India'

print(str + str1)
print(str+" "+str1)

# In python we can't combine or concate number using + oprator for that we can used format

age=25
txt='My name is khan and my age is {}'
print(txt.format(age))

Qty=5
ItemNo=58
INR=1000

text='I want {} qty of this item no {} in {}/- only'
print(text.format(Qty,ItemNo,INR))

#capitalize()	Converts the first character to upper case

stext='akshay'
print(stext.capitalize())

#casefold()	Converts string into lower case
stext2='AKSHAY'
print(stext2.casefold())

#center()	Returns a centered string taking up the space of 6 characters
stext3='I Love India'
print(stext3.center(6))

#count()	Returns the number of times a specified value occurs in a string
print(stext3.count('I'))

#encode()	Returns an encoded version of the string
ss=stext3.encode()
print(ss)

#endswith()	Returns true if the string ends with the specified value
print(stext3.endswith('4')) #False
print(stext3.endswith('a'))#true

#expandtabs()	Sets the tab size of the string
stext4='I\tLove\tIndia'
print(stext4.expandtabs(56))

#find()	Searches the string for a specified value and returns the position of where it was found
#index()	Searches the string for a specified value and returns the position of where it was found
print(stext3.find('L'))
print(stext3.index("n"))


"""isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""


