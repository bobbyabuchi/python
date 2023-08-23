# notes from w3schools.com

# ..........................................................................Python Data Types

x = 5
print(type(x))

# a dictionary of some data types in Pyhton
python_data_types = {
    "str": 'x = "Hello Bob"', 
    "int":'x = 2022',
    "float":'x = 09.29',
    "complex":'5j',
    "list":'["cars", "computers", "phones"]',
    "tuple":'("notes", "pen", "texts")',
    "range":'range(8)',
    "dict":'{"name": "Bobby", "age": 32}',
    "set":'{"bananas", "twining", "berries"}',
    "frozenset":'({"bananas", "twining", "berries"})',
    "bool":'True',
    "bytes":'b"Word"',
    "bytearray":'bytearray(5)',
    "memoryview":'memoryview(bytes(5))',
    "NoneType":'None'
}

# one can acutally set a specific data type, especially if you left C/C++ but they haven't left you
# just invoke the data type as a method
x = str("Hello World")
x = int(20)
x = float(20.22)

# ..........................................................................Python Numbers

# three numeric types (int, float and complex) in Python
a = 13
b = 20.22
c = 1j
d = 12E4    # float
e = 10e22   # still float


# verify type of an object
print(type(a),type(b),type(c),type(d),type(e))

# random numner
from operator import le
import random
print(random.randrange(1, 10)) # display a random number from 1 - 9, excluding 10 

# ..........................................................................Python Casting
# this is the same as specify a variable type
# done with constructor functions int(), float(), str()

# convert float to int
a = 22.20
print(int(a)) # prints 22

# ..........................................................................Python Strings

# multiline strings with double or single qoute
a = """
This is a multiline string
will read and interpret the white spaces and 
line breaks
"""
print(a)

# arrayish nature of strings
a = "Hello, Word!"
print(a[0])

# loop through a string
a = "BobbyAbuchi"
for b in a:
    print(b)
print(len(a))

# scan a text for a bunch of characters
c = "The lines are fallen unto me in pleasant places! I have a godly heritage."
print("godly" in c)

if "godly" in c:
    print("Yes, he said godly.")

if "agwa" not in c:
    print("No mention of agwa here.") 

# slicing strings - this counts commas and white spaces
a = "ABCDE,EFGH IJKL"
print(a[2:6])

# slice from start
print(a[:5])

# slice to end
print(a[3:])

# negative indexing
print(a[-6:-2])

# with python built-in methods, you can modify strings
name = "BobbyAbuchi"
print(name.upper())
print(name.lower())
print(name.replace("Bobby", "Nonso"))

#split into subsrings
name = "Bobby Abuchi"
name = name.split(" ") # space, comma, character
print(name)

name = "Bobby"
color = "Navy"
number = 1101
print("My name is {}, color is {} and number is {}.".format(name,color,number))

# use index numbers to place correctly
print("My number is {2}, color is {1} and name is {0}.".format(name,color,number))

# just name the indexs
print("My color is {color}, name is {name} and number is {number}.".format(name = name, color = "Blue", number = number))

# format decimal
total_price = 50
cart = "The total price of goods ordered is {:.2f} Naira."
print(cart.format(total_price))

# ..........................................................................Python Booleans

# ..........................................................................Python Operators

# ..........................................................................Python Lists

a = [1,2,3,4,5,6,7]
print(a)
a.insert(0, 10)     # place 10 in firt slot
print(a)
a[-1] = 700         # change the last item 7 to 700
print(a)

# loop through a list with range and length of list
a = [1,2,'trinity',4,'grace',6,'perfect',8,'infinitum',10]
for x in range(len(a)):
    print(x)                # don't be fooled, this will only print number 0 to 9, your usual range function
    print(a[x])             # this is what will actually loop through the content targeting their index

# using a while loop
b = [1,2,'trinity',4,'grace',6,'perfect',8,'infinitum',10]
x = 0
while x < len(b):
    print(b[x])
    x +=1

# list comprehension: alist = [expression for item in iterable if condition == True] 
c = [1,2,'trinity',4,'grace',6,'perfect',8,'infinitum',10]
[print(x) for x in c]

d = ['trinity','grace','perfect','infinitum']
e = [x for x in d if "r" in x]
print(e)

d = ['trinity','grace','perfect','infinitum']
e = [x.upper() for x in d]
print(e)

d = ['trinity','grace','perfect','infinitum']
d.sort(reverse=True)
print(d)

water = ["H",2,"O"]
oxygen = ["O",2]
for x in oxygen:
    water.append(x)
print(water)

h = ["H2"]
o = ["O"]
h.extend(o)
print(h)

# ..........................................................................Python Tuples

# because they're immutable, you've got to convert them to list, add to them and take back to tuple
os = ("Windows", "Linux", "MAC")
moreOs = list(os)
print(moreOs) 
moreOs.append("Android") 
moreOs.append("IOS")
print(moreOs)
os = tuple(moreOs)
print(os)

# upack tuples - the process of extracting tuple values back to unit variables

profile = ("Bobby", "Business Analyst", "Pinterest", "Dublin")
(name, role, company, county) = profile

print(name, role, company, county)

# the number of variables for unpacking must match the number of items in tuple, else, 
# use "the asterisk" to package the remaining items as a list, in the last variable
profile = ("Bobby", "Business Analyst", "Pinterest", "Dublin", 5.0, "Python", "C++", "Flask", "Django", "Azure", "AWS")
(name, role, company, county, *others) = profile

print(name, role, company, county, others)

profile = ("Bobby", "Business Analyst", "Pinterest", "Dublin", 5.0, "Python", "C++", "Flask", "Django", "Azure", "AWS")
(name, role, *company, county, others) = profile

print(name, role, company, county, others)

a = []
b = (2,4,6,8)
for x in b:
    x = x*2
    a.append(x) 
print(a)

# find the index
phone = (8,0,3,7,7,5,6,7,1,1,)
x = phone.index(7) # target index value of the first occurence of the number 7
print(x)

# ..........................................................................Python Sets

# join two sets
drinks = {"Water", "Sprite", "Wine", "Tea", "Juice"}
favs = {"Cake", "Bread", "Biscuits", "Apples", "Bananas"}
# .union()
launch_set = drinks.union(favs)
print(launch_set)
# .update() 
drinks.update(favs)
print(drinks)

# .intersection_update() method will keep only the items that are present in both sets
first_round = {"Bobby", "Vesper", "Reycruise", "Markachi", "Wind"}
second_round = {"Bobby", "Markachi", "Mark", "AirboneMaC"}
first_round.intersection_update(second_round)
print(first_round)

# .intersection_update() method will return a new set with the items that are present in both sets
first_round = {"Bobby", "Vesper", "Reycruise", "Markachi", "Wind"}
second_round = {"Bobby", "Markachi", "Mark", "AirboneMaC"}
third_round = first_round.intersection(second_round)
print(third_round)

# .symmetric_difference_update() keep only the elements that are NOT present in both sets
first_round = {"Bobby", "Vesper", "Reycruise", "Markachi", "Wind"}
second_round = {"Bobby", "Markachi", "Mark", "AirboneMaC"}
first_round.symmetric_difference_update(second_round)
print(first_round) # vesper rey wind air

# .symmetric_difference() return a new set with that contains all items from both sets, except items that are present in both sets
first_round = {"Bobby", "Vesper", "Reycruise", "Markachi", "Wind"}
second_round = {"Bobby", "Markachi", "Mark", "AirboneMaC"}
third_round = first_round.intersection(second_round)
print(third_round)

# other set methods -- Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

# ..........................................................................Python Dictionaries

user = {
    "first_name": "Bobby",
    "last_name": "Abuchi",
    "username": "bobbyabuchi",
    "status": "registered"
}
print(user)
print(len(user))
print(user["username"])
print(user.get("status"))
print(user.keys())
print(user.values())

# add a new item to the dictionary
user["email"] = "bobbyabuchi@gmail.com"
print(user)

# check if a key is present
user = {
    "first_name": "Bobby",
    "last_name": "Abuchi",
    "username": "bobbyabuchi",
    "status": "registered"
}
if "status" in user.keys():
  print("Yes, 'status' is a key in the dictionary")
else:
    print("No it's not, check the values")

# check for a value
if "registered" in user.values():
  print("Yes, 'registered' is a value in the dictionary")
else:
    print("No it's not")

# change dicionary value
user["last_name"] = "Airborne"
user.update({"first_name": "Mark"})
print(user)

# add items
user["phone"] = "08037756711"
user.update({"Country": "Ireland"})

# nested dictionary
profile = {
    "users": user,
    "data_type": python_data_types
    }

# ..........................................................................Python If...Else

# short hand if...else
a = input("Enter password: ")
b = input("Confirm password: ")
print("Passwords don't match!") if a != b else print("Password set!")

# short hand 3 conditions
score = int(input("Enter score: "))
print("Excellent") if score >= 70 else print("Good") if score >= 69 else print("Fair")


# ..........................................................................Python While Loops

# with break statement u can stop the loop even while the condition is true


# ..........................................................................Python For Loops

for a in range(6):
    print(a)

else:
    print("Boom!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

yearGroup = [1,2,3,4,5,6]
classGroup = ["A","B","C","D","E"]
time_period = ["Alpha", "Omega"]
for a in yearGroup:
    for b in classGroup:
        for c in time_period:
            print(a,b,c)

pem = "CAT"
pem = list(pem)
b = len(pem)
mn = b - 1


# ..........................................................................Python Functions

def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

# ..........................................................................Python Lambda

i = lambda a : a + 10
print(i(5))

total = lambda a, b, c, d : a+b+c+d
print(total(10, 40, 20, 30))

name = lambda user: user
print(name("Bobby"))

# ..........................................................................Python Arrays

# ..........................................................................Python Classes/Objects

#  creating class Users, a blue print for all users 
class Users:
    # with the __init__() assign values to object properties or operations needed when object is created
    def __init__(self, name, username, code):
        self.name = name
        self.username = username
        self.code = code

    # __str__() controls what should be returned...when class object be string else the object is returned
    def __str__(self): # string rep of an object
        return f"{self.name}({self.code})"

    # object method
    def UserFunc(self):
        print("Hi my name is " + self.name)

user1 = Users("Bobby", "bobbyabuchi", 1101)

print(user1.name, user1.username, user1.code)
user1.UserFunc()

# ..........................................................................Python Inheritance

# ..........................................................................Python Iterators

a = "ube"
b = iter(a)
print(next(b))
# ..........................................................................Python Scope

# ..........................................................................Python Modules

# ..........................................................................Python Dates

# ..........................................................................Python Math

# ..........................................................................Python JSON

# ..........................................................................Python RegEx

# ..........................................................................Python PIP

# ..........................................................................Python Try...Except

# ..........................................................................Python User Input

# ..........................................................................Python String Formatting

import os
print(os.name)
print(os.getcwd())

# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
	if l==r:
		print (toString(a))
	else:
		for i in range(l,r):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)

# This code is contributed by Bhavya Jain