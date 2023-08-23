"""
Functions and Tuples
In week three you will be introduced to the construction of functions.
write your own functions, including how to define a function, how to incorporate parameters,
how to return data from a function, the local or global scope of variables, and potential side effects that could occur from function execution.
Finally, we look at tuples more in depth, and how automatic packing and unpacking of tuples can be used in functions and in for loops.
"""
# Default Parameter Value : The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def nationality(country = "Black", ZipCode = 'Enter Zipcode'):
  print("I am from " + country, ZipCode)
nationality("Sweden")
nationality("India")
nationality('Israel')
nationality("Brazil", 270)
nationality()

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values: To let a function return a value, use the return statement:
def times_5(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# 12.2. Function Definition

def square(x):
    y = x * x
    return y # returns the value of the expression y = x * x

nomba = 10
result = square(nomba)
print("The result of {} squared is {}.".format(nomba, result))

z = square(4)
print(z)

def longer_than_five(list_of_names):
    for name in list_of_names: # iterate over the list to look at each name
        if len(name) > 5: # as soon as you see a name longer than 5 letters,
            return True # then return True!
            # If Python executes that return statement, the function is over and the rest of the code will not run -- you already have your answer!
    return False # You will only get to this line if you
    # iterated over the whole list and did not get a name where
    # the if expression evaluated to True, so at this point, it's correct to return False!

# Here are a couple sample calls to the function with different lists of names. Try running this code in Codelens a few times and make sure you understand exactly what is happening.

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))

def show_me_numbers(list_of_ints):
    print(10)
    print("Next we'll accumulate the sum")
    accum = 0
    for num in list_of_ints:
        accum = accum + num
    return accum
    print("All done with accumulation!")

show_me_numbers([4,2,3])


# Write a function named same that takes a string as input, and simply returns that string.
def same(x):
    return x
same('Bondar')

# Write a function named intro that takes a string as input. Given the string “Becky” as input,
# the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(x):
    z =('Hello, my name is '+ x +' and I love SI 106.')
    return z
intro('Becky')

# 14. Write a function called decision that takes a string as input, and then checks the number of characters.
# If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return
# “This is a short string”.
def decision(st):
    x = len(st)
    if x > 17:
        return 'This is a long string'
    else:
        return 'This is a short string'
# Alternatively...
def decision2(st):
    x = len(st)
    if x > 17:
        return 'This is a long string'
    return 'This is a short string'

# 12.7. A function that accumulates

# custom made len()
def my_len(seq):
    c = 0 # initialize count variable to 0
    for each_unit in seq:
        c += 1   # increment the counter for each item in seq
    return c
print(my_len("hello"))
print(my_len([1, 2, 7]))

# Write a function named total that takes a list of integers as input, and returns the total value
# of all those integers added together.
def total(x):
    c = 0
    for j in x:
        c = j + c
    return c
total([1, 2, 4])

# Write a function called count that takes a list of numbers as input and returns a count of the
# number of elements in the list.
def count(x):
    c = 0
    for i in x:
        c += 1
    return c
count([1,2,3,4,5])

# Let’s use composition to build up a little more useful function. Recall from the dictionaries chapter
# that we had a two-step process for finding the letter that appears most frequently in a text string:
# 1. Accumulate a dictionary with letters as keys and counts as values. See example.
# 2. Find the best key from that dictionary. See example.
# We can make functions for each of those and then compose them into a single function that finds
# the most common letter.
def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))

# Write two functions, one called addit and one called mult. addit takes one number as an input
# and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned
# by addit, and then returns the result.
def addit(x):
    return x + 5

def mult(y):
    return addit(y) * y

print(mult(4))

# Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(lst):
    total = 0
    for each_int in lst:
        total = total + each_int
    return total

lst = [13,10,1989]

print(accum(lst))

# Write a function, length, that takes in a list as the input. If the length of the list is greater
# than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(lst):
    if len(lst) >= 5:
        return 'Longer than 5'
    return 'Less than 5'
lst = [1,2,3,4,5]
print(length(lst))

# You will need to write two functions for this problem. The first function, divide that takes in any
# number and returns that same number divided by 2. The second function called sum should take any
# number, divide it by 2, and add 6. It should return this new number.
# You should call the divide function within the sum function. Do not worry about decimals.
def divide(x):
    return x/2

def sum(x):
    return divide(x) + 6

print(sum(10))

#  Below, we have provided a list of tuples. Write a for loop that saves the second element
#  of each tuple into a list called seconds.
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = []
for each_tuple in tups:
    c = list(each_tuple)
    seconds.append(c[1])
print(seconds)

# 13.3. Tuple Assignment with Unpacking

# unpacking tuple of values into the variable names.
# This does the equivalent of seven assignment statements, all on one easy line.
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia
# Naturally, the number of variables on the left and the number of values on the right have to be the same.
name = julia[0]
surname = julia[1]
print(name,surname)

# Unpacking into multiple variable names also works with lists, or any other sequence type,
# as long as there is exactly one value for each variable. For example, you can write x, y = [3, 4]

# 13.3.1. Swapping Values between Variables
a = 1
b = 2
temp = a # temp1
a = b # a2
b = temp # b1
print(a, b, temp) # 2,1,1

# Tuple assignment solves this problem neatly:
a = 1
b = 2
(a, b) = (b, a)
print(a, b) # 2,1

# The left side is a tuple of variables; the right side is a tuple of values. Each value is assigned to its
# respective variable. All the expressions on the right side are evaluated before any of the assignments.
# This feature makes tuple assignment quite versatile

# 13.3.2. Unpacking Into Iterator Variables

# Multiple assignment with unpacking is particularly useful when you iterate through a list of tuples.
# You can unpack each tuple into several loop variables. For example:
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy'), ('Bobby', 'Abuchi')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)

# On the first iteration the tuple ('Paul', 'Resnick') is unpacked into the two variables first_name and last_name.
# On the second iteration, the next tuple is unpacked into those same loop variables.

# 13.3.3. The Pythonic Way to Enumerate Items in a Sequence

#  iterating through the indexes of a sequence, and thus enumerate the items and their positions in the sequence
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

# Python provides a built-in function enumerate. It takes a sequence as input and returns a sequence of tuples.
# In each tuple, the first element is an integer and the second is an item from the original sequence.
# (It actually produces an “iterable” rather than a list, but we can use it in a for loop as the sequence
# to iterate over.)

# more pythonic approach to enumerating items in a sequence.
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# With only one line of code, assign the
# variables: water, fire, electric, and grass to the values “Squirtle”, “Charmander”, “Pikachu”, and “Bulbasaur”
(water, fire, electric, grass) = ("Squirtle", "Charmander", "Pikachu", "Bulbasaur")

# If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind,
# we have provided you a dictionary called pokemon. For every key value pair, append the key to the list p_names,
# and append the value to the list p_number. Do not use the .keys() or .values() methods.

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
pokemon = pokemon.items()
#print(pokemon)
p_names = []
p_number = []
for k in pokemon:
    c = list(k)
    #print(c)
    p_names.append(c[0])
    p_number.append(c[1])
print(p_names,p_number)

# The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list
# of keys from the dictionary track_medal_counts and assign the list to the variable name track_events.
# Do NOT use the .keys() method.
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events = []
track_medal_counts = track_medal_counts.items()
for events in track_medal_counts:
    events = list(events)
    track_events.append(events[0])
print(track_events)
track_events = track_medal_counts

# 13.4. Tuples as Return Values

# Functions can return tuples as return values. This is very useful — we often want to know some batsman’s highest
# and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month,
# and the day, or if we’re doing some ecological modeling we may want to know the number of rabbits and the number
# of wolves on an island at a given time. In each case, a function (which can only return a single value),
# can create a single tuple holding multiple elements.

# For example, here is a function that returns both the area and the circumference of a circle of radius r.
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r         # 2Pr
    a = 3.14159 * r * r         # Pr2
    return (c, a)

print(circleInfo(10))

# Again, we can take advantage of packing to make the code look a little more readable on line 5
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a
print(circleInfo(int(input('Enter radius: '))))

# It’s common to unpack the returned values into multiple variables.
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)

# Define a function called information that takes as input, the variables name, birth_year, fav_color, and
# hometown. It should return a tuple of these variables in this order.
def information(name, birth_year, fav_color, hometown):
    return name, birth_year, fav_color, hometown,

# Define a function called info with the following required parameters: name, age, birth_year, year_in_college,
# and hometown. The function should return a tuple that contains all the inputted information.
def info(name, age, birth_year, year_in_college, hometown):
    return name, age, birth_year, year_in_college, hometown

# 13.5. Unpacking Tuples as Arguments to Function Calls

# Python even provides a way to pass a single tuple to a function and have it be unpacked for assignment
# to the named parameters.

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(z)) # this line causes an error

# This won’t quite work. It will cause an error, because the function add is expecting two parameters,
# but you’re only passing one parameter (a tuple). If only there was a way to tell python to unpack
# that tuple and use the first element to assign to x and the second to y.
#
# Actually, there is a way.

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked

# 13.6. Glossary
# tuple
# A type of sequence, much like a list but immutable. A tuple is created by enclosing one or more values in
# parentheses, separated by commas.
#
# packing
# When multiple values are specified, separated by commas, they are packed into a tuple.
#
# unpacking
# When a tuple is assigned to a collection of variable names separated by commas, the tuple is unpacked and
# the separate values are assigned to each of the variables.
#
# pair
# A tuple with exactly two items.

# Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in
# the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country.
# You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method.

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals = []
g_old = gold.items()
for medals in g_old:
    medals = list(medals)
    num_medals.append(medals[1])
print(num_medals)