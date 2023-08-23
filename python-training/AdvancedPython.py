import psycopg2

# loop through a string
for x in "banana":
  x *= 3
  print(x)

# Check for string in a string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Get 'llo'
b = "Hello, World!"
print(b[2:5])

# say 'Hello' 
b = "Hello, Word!"
print(b[:5])

# Get the 'Word'!
b = "Hello, Word!"
print(b[6:11])

# loud the 'Word!'
b = "Hello, Word!"
print(b[6:])

# Negative Indexing
name = 'Bobby'
print(name[-1])
print(name[-5])
print(name[-5:-2]) # Bob

# remove white space
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

a = "Every human being is a puzzle of need."
print(a.split(" "))

# Formating Strings
age = 36
txt = "My name is John, I am {}."
print(txt.format(age))

current_year = 2021
yob = 1989
age = (current_year - yob)
name = 'Bobby Abuchi'
aos = 'Python Developer'
country = 'Nigeria'

bio = "My name is {}, I was born in {} am {}, a {}, {}."
print(bio.format(name, yob, age, aos, country))

print(bool("abc"))

# insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Add List B to List A
A = ["apple", "banana", "cherry"]
B = ["mango", "pineapple", "papaya"]
A.extend(B)
print(A)

# The extend() method adds any iterable, it does not have to 
# append lists, you can add any iterable object 
# (tuples, sets, dictionaries etc.).
A_list = ["apple", "banana", "cherry"]
B_tuple = ("kiwi", "orange")
A_list.extend(B_tuple)
print(A_list)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ("apple", "banana", "cherry")
print(fruits[2])

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
print(fruits.update(more_fruits))

# Loop Through the Index Numbers: Print all items by referring to their index number
fruit_list = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i,fruit_list[i])

# A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# so this will loop through ...
SavioursResort = ["Chapel", "Kitchen", "Garden", "Accomodation", "Ofice Space"]
newlist = []

for x in SavioursResort:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5] 
print(newlist)

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits] 

newlist = ['hello' for x in fruits] 
print(newlist)

