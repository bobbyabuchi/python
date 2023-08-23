# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]

# 23.1. Introduction: Map, Filter, List Comprehensions, and Zip
'''
Like in the accumulator pattern, We have frequently taken a list and produced another list from it that contains
either a subset of the items or a transformed version of each item
 -> When each item is transformed we say that the operation is a mapping, or just a map of the original list.
 -> When some items are omitted, we call it a filter.
 -> Python provides a new syntax, called list comprehensions, that lets you express a mapping and/or filtering
operation. Both map and filter are built-in functions in Python.
'''
# Map, and filter are commands that you would use in high-performance computing on big datasets.

# 23.2. Map

'''
Python map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax: ->  map(fun, iter)
'''


# The following function produces a new list with each item in the original list doubled.
# It is an example of a mapping,
# from the original list to a new list of the same length, where each element is doubled.
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

'''
The doubleStuff function is an example of the accumulator pattern, in particular the mapping pattern. On line 3, 
new_list is initialized. On line 5, the doubled value for the current item is produced and on line 6 it is appended 
to the list we’re accumulating. Line 7 executes after we’ve processed all the items in the original list: 
it returns the new_list.
'''
# As we did when passing a function as a parameter to the sorted function, we can specify a function to pass to map
# either by referring to a function by name, or by providing a lambda expressi
def triple(a):
    return 3*a
#--------------------------------------------
def tripleStuff(b):
    newStuff = map(triple, b)
    return list(newStuff)
#--------------------------------------------
print(tripleStuff('Bobby & Chisom'))
def quadStuff(c):
    newStuff = map(lambda value: 4*value, c)
    return list(newStuff)
#-------------------------------------------
print(triple(160))
L = [2, 5, 9, 10]
print(L)
print('------------------------------------')
Lx3 = tripleStuff(L)
print(Lx3)
print('------------------------------------')
Lx4 = quadStuff(L)
print(Lx4)

# Of course, once we get used to using the map function, it’s no longer necessary to define functions like
# tripleStuff and quadStuff.
L = [2, 5, 9, 10]

Lx4 = map((lambda value: 4*value), L)
print(list(Lx4))

# or all on one line
print(list(map((lambda value: 5*value), [2, 5, 9, 10])))

# 1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map((lambda x: 2*x), lst)
print(list(greeting_doubled))

# 2. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper
# that contains all the same strings in upper case.
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = map((lambda x: x.upper()), abbrevs)
print(list(abbrevs_upper))

# 23.3. Filter: going through a list and keeping only those items that meet certain criteria.

def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

# the filter function takes two arguments, a function and a sequence. The function takes one item and return True
# if the item should. It is automatically called for each item in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.
def get_evens(n):
    v = filter(lambda x: x % 2 == 0, n)
    return list(v)

print(get_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#  Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

def check_w(lst):
    myV = []
    for a in lst:
        if 'w' in a:
            myV.append(a)
    return list(myV)
filter_testing  = filter(check_w, lst_check)
print(check_w(lst_check))

# 2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2.
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

def check_o(lst):
    myV = []
    for a in lst:
        if 'o' in a:
            myV.append(a)
    return list(myV)
lst2  = filter(check_o, lst)
print(lst2)

# 23.4. List Comprehensions
# Python's alternative way to do map and filter operations.

# List comprehensions are concise ways to create lists from other lists. The general syntax is:
# [<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]

# where the if clause is optional. For example
things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)
# where the transformer expression is -> value * 2
# item variable is -> value
# sequence is -> things
'''
As with map, each item in the sequence is transformed into an item in the new list. Instead of the iteration happening 
automatically, however, we have adopted the syntax of the for loop which may make it easier to understand.

Just as in a regular for loop, the part of the statement for value in things says to execute some code once for each 
item in things. Each time that code is executed, value is bound to one item from things. The code that is executed 
each time is the transformer expression, value * 2, rather than a block of code indented underneath the for statement. 
The other difference from a regular for loop is that each time the expression is evaluated, the resulting value is 
appended to a list. That happens automatically, without the programmer explicitly initializing an empty list or 
appending each item.
'''

# The if clause of a list comprehension can be used to do a filter operation.
# To perform a pure filter operation, the expression can be simply the variable that is bound to each item.
# For example, the following list comprehension will keep only the even numbers from the original list.
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list
print(keep_evens([3, 4, 6, 7, 0, 1]))

# combining map and filter operations (by chaining them together, or with a single list comprehension).
things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])

# AdAccum-4-1: What is printed by the following statements?
alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1] # will check for odd num first then double
print(blist) #  5 is the only odd number in alist. It is doubled before being placed in blist.

# 2. The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to
# accomplish the same thing. Assign it the the variable lst2. Only one line of code is needed.
L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)
# using list comprehension
lst2 = [n for n in L if n > 10]
print(lst2)

# 3. Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the
# dictionary tester. Do this using a list comprehension.

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
x = tester.values()
'''
compri = []
for a in x:
    c = a
    for b in c:
        d = b['name']
        compri.append(d)
        print(b['name'])
print(compri)
'''
# Using list comprehension
compri = [b['name'] for a in x for b in a]
print(compri)

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
innerList = tester['info']
#print(innerList)
#if i want to pretty print, using json.dumps()
#import json
#print(json.dumps(innerList, indent=2))
compri = [d['name'] for d in innerList]
print(compri)

# Comprehending List Comprehension
#-----------------------------------------------------------------------------------
L = [1,2,3,4,5]
var_items = [x for x in L]

# Using Conditionals with List Comprehensions: utilize conditional statements to modify existing lists or other
# sequential data types when creating new lists.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)
#---------------------------------------------------------------------
# this code
my_list = []
for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)
print(my_list)
# is the same as this (using list comprehension)
my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(my_list)
#-------------------------------------------------------------------

# Nested Conditionals
L = [i for i in range(8) if i%2==0 if i%3==0]

# if..else in List Comprehension
A = ["Even" if i%2==0 else "Odd" for i in range(8)]

# Dict Comprehension
d1 = {str(i):i for i in [1,2,3,4,5]}    # create dict with numbers as values
print(d1)
fruits = ['apple', 'mango', 'banana','cherry']
# dict comprehension to create dict with fruit name as keys
d2 = {f:len(f) for f in fruits}
print(d2)

# elements of the list as the keys and the elements with first letter capitalized as the values.
d3 = {f:f.capitalize() for f in fruits}

# dict comprehension example using enumerate function
fruits = ['apple', 'mango', 'banana','cherry']
d4 = {f:i for i,f in enumerate(fruits)}       # enumerate takes an iterable as input, returns its elements and index

# dict comprehension example to reverse key:value pair in a dictionary
f_dict = {f:i for i,f in enumerate(fruits)}

L6 = {'apple': 0, 'banana': 2, 'cherry': 3, 'mango': 1}
# dict comprehension to reverse key:value pair in a dictionary
d6 = {v:k for k,v in f_dict.items()}

# 23.5. Zip:

# looping through the possible index values
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):        # take into account the length of the lists
    L3.append(L1[i] + L2[i])    # in this case add index0 of L1 and index0 of L2, then index1 and index2
print(L3)                       # should yield [4, 6, 8]

# The zip function takes multiple lists and turns them into a list of tuples..., pairing up all the first items as one tuple,...
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = zip(L1, L2)            # will return a <zip object at 0x00000085E68CE3C8>
L4 = list(zip(L1, L2))      # will return a list of tuples [(3, 1), (4, 2), (5, 3)]
print(L3)
print(L4)

# when you loop through the tuples
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))
print(L4)
for (x, y) in L4:       # for the 2 pairs in each element of L4 tuples
    L3.append(x+y)      # add the 2 pairs
print(L3)

# using a list comprehension:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x + y for (x, y) in list(zip(L1, L2))]
print(L3)

# using map (and not unpacking the tuple)
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(L3)
print(list(L3))

# Consider a function called possible, which determines whether a word is still possible to play in a game of hangman,
# given the guesses that have been made and the current state of the blanked word.
# Below we provide function that fulfills that purpose.
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True
print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# However, we can rewrite that using zip, to be a little more comprehensible.
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True
print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

# 1. Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3,
# that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5.
# This can be accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [a+b for (a,b) in list(zip(L1,L2)) if a > 10 if b < 5]
print (L3)

#------------------------------------------Assessment---------------------------------------------
# 1. Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ”
# to the beginning of each element using mapping.
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
def addStr(a):
    for i in a:
        i = 'Fruit: ' + a
        return i
map_testing  = map(addStr, lst_check)
print(list(map_testing))

# 2. Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
def check_b(a):
    BL = []
    for x in a:
        if 'B' in a[0]:
            BL.append(a)
    return list(BL)
b_countries = filter(check_b, countries)
print(b_countries)

# 3. Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names  = [a[1] for a in people]

# 4. Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [x*2 for x in lst]

# 5. Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [x for x,y in students if y >= 70]

#. 6 Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
# 100% score
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = zip(l1, l2)
opposites = list(filter(lambda s: len(s[0])>3 and len(s[1])>3, l3))
print(opposites)
# my solution 80% score
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = [(a,b) for a,b in list(zip(l1,l2)) if len(a) > 3 if len(b) > 3]
print(opposites)
# another 100%
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda a: (len(a[0]) > 3 and len(a[1]) > 3), zip(l1, l2)))

# 7. Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
s = species
p = population
pop_info = zip(s,p)
endangered = [s for s,p in pop_info if p <= 2500]