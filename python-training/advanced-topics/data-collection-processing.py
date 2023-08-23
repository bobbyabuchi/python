# Data Collection and Processing (Week 1) -------------------------------------------

# 17.1. Introduction: Nested Data and Nested Iteration

# 17.1.1. Lists with Complex Items

# the items in a list can be any type of python object. For example, we can have a list of lists.
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
print("-------")
for L in nested1:
    print(L)

# With a nested list, you can make complex expressions to get or set a value in a sub-list.
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])

# You can change values in such lists in the usual ways. You can even use complex expressions to change values.
# Consider the following
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
nested1[1] = [1,2,3]
nested1[1][0] = 100
print(nested1)

# You can even have a list of functions (!)

def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

# In this first for loop, we do not call the functions, we just output their printed representations.
print("****names****")
for each_item in L:
    print(each_item)
# here, we call each of the functions, passing in the value -2 each time and printing whatever value the function returns.
print("****call each of them****")
for each_item in L:
    print(each_item(-2))

print("****just the first one in the list****")
print(L[0])     # picks out the function square
print(L[0](3))  # picks out the function square and pass the value 3 as a parameter

# 1. Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]
idx1 = animals[1][0]

# 2. Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = data[7][0][0]

# 17.2. Nested Dictionaries

"""
In particular, it is often useful to have a list or a dictionary as a value in a dictionary. And of course, 
those lists or dictionaries can also contain lists and dictionaries. There can be many layers of nesting.
-> Only the values in dictionaries can be objects of arbitrary type. 
The keys in dictionaries must be one of the immutable data types (numbers, strings, tuples).
"""
d = {'A':1, 'B':2, 'C':3, 'X':3, 'Y':4, 'Z':5}
for x in d:
    print(d[x])
for x in d.values():
    print(x)
# so with the above example, you'll know to handle a nested dictionary at any level...

# you can Loop through both keys and values, by using the items() function
d = {'A':1, 'B':2, 'C':3, 'X':3, 'Y':4, 'Z':5}
for x, y in d.items():
    print(x,y)

# changing values: change the value of a specific item by referring to its key name
date = {'D':20,'M':'Feb','Y':2020}
print('1.',date)
date['Y'] = 1989
date['M'] = 'Oct'
date['D'] = 13
print('2.',date)

# assigning/changing values...this time a dictionary as value...
date = {'D':20,'M':'Feb','Y':2020}
date['M'] = {
'M1':'January','M2':'February','M3':'March','M4':'April',
'M5':'May','M6':'June','M7':'July','M8':'August',
'M9':'September','M10':'October','M11':'November','M12':'December'
}
print(date)

# 1. Extract the value associated with the key color and assign it to the variable color. Do not hard code this.
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
color = info['personal_data']['physical_features']['color']
print(color)

# write some legal assignment statement, after the following code executes (from my observation, keys do not really change, but values can be reassigned)
d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
print(d, 'length =', len(d))
d[5] = {1: 2, 3: 4}     # in this case added an item with key '5' and a {dictionary} as its value
print(d, 'length =', len(d))
d['key1']['d'] = d['key2']  # here a new key 'd' is created in 'key1' with replica of dictionar values of 'key2'
print(d, 'length = ', len(d))
print(d['key1'], 'length = ', len(d['key1']))

# 17.3. Processing JSON results
"""
JavaScript Object Notation [JSON] looks a lot like the representation of nested dictionaries and lists in python 
when we write them out as literals in a program, but with a few small differences (e.g., the word null instead of None).
-> When your program receives a JSON-formatted string, generally you will want to convert it into a python object, 
a list or a dictionary.
-> Again, python provides a module for doing this. The module is called json. We will be using two functions in this 
module; 
    -> json.loads(): takes a string as input and produces a python object (a dictionary or a list) as output 
    -> json.dumps(): loads turns a json-formatted string into a list or dictionary
"""
# Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
a_str = '\n{\n"resultCount":25, \n"results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
print(a_str)
d = json.loads(a_string)
print("------")
print(d)
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])

"""
The other function we will use is dumps. It does the inverse of loads. It takes a python object, typically a dictionary 
or a list, and returns a string, in JSON format. It has a few other parameters. Two useful parameters are sort_keys and 
indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic 
order with their values. The indent parameter expects an integer. When it is provided, dumps generates a string suitable 
for displaying to people, with newlines and indentation for nested lists or dictionaries. For example, the following 
function uses json.dumps to make a human-readable printout of a nested data structure.
"""
import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

# 17.4. Nested Iteration
# When you have nested data structures, especially lists and/or dictionaries, you will frequently need nested for loops to traverse them.
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

# my nesting...
nesting = ['Gabriel & Eunice', 'Aaron & Monica', ['Sid & Victoria', 'Chukwuemeka & Matilda', ['Bobby & Chisom']]]
for x in nesting:
    for y in x:
        for z in y:
            l3 = z
        l2 = y
    l1 = x
print(y)

print('Grand Parents...: ', nesting[0], ',', nesting[1],)
print('Parents.........: ', nesting[2][0], ',', nesting[2][1])
print('Children........: ', nesting[2][2][0])

# make a function that counts all the *leaf* items in a nested list like nested1 above, the items at the lowest level of nesting (8 of them in nested1).
def count_leaves(n):
    count = 0
    for L in n:
        for x in L:
            count = count + 1
    return count
n = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
print(count_leaves(n))
8
# 2. Below, we have provided a list of lists that contain information about people. Write code to create a new list that
# contains every person’s last name, and save that list as last_names.

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'],
        ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for n in info:
    last_names.append(n[1])
print(last_names)

# Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []
for n in L:
    for a in n:
        if 'b' in a:
            b_strings.append(a)
print(b_strings)

# 17.5. 👩‍💻 Structuring Nested Data

"""
When constructing your own nested data, it is a good idea to keep the structure consistent across each level. 
For example, if you have a list of dictionaries, then each dictionary should have the same structure, meaning 
the same keys and the same type of value associated with a particular key in all the dictionaries. The reason 
for this is because any deviation in the structure that is used will require extra code to handle those special cases. 
The more the structure deviates, the more you will have to use special cases.
"""
# For example, let’s reconsider this nested iteration, but suppose not all the items in the outer list are lists.
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    print(x)
    for y in x:
        print("     level2: {}".format(y))
# Now the nested iteration fails.

#...should be written this way with special casing, a conditional that checks the type before iterating
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)

# 17.6. Deep and Shallow Copies
"""
Earlier when we discussed cloning and aliasing lists we had mentioned that simply cloning a list using [:] would take 
care of any issues with having two lists unintentionally connected to each other. That was definitely true for making 
shallow copies (copying a list at the highest level), but as we get into nested data, and nested lists in particular, 
the rules become a bit more complicated. 
We can have second-level aliasing in these cases, which means we need to make deep copies.

When you copy a nested list, you do not also get copies of the internal lists. ***(this is a tricky situation)
This means that if you perform a mutation operation on one of the original sublists, 
the copied version will also change. We can see this happen in the following nested list, which only has two levels.
"""
# this is how you clone a list
L = ['SE','ML', 'AI', 2020, ['Python', 'JSON', 'SQL',['Gifted','Open Door',['To', 'the', 'Glory', 'of', 'God']]]]
print('Original L',L)
L2 = L[:]
L[2] = 'DL'                 # this modification will NOT affect the copy
L[4][3][0] = 'Very Gifted'  # this modification will affect the copy
L.append('AI')
print('L: ',L)
print('L2: ', L2)

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied = original[:]
print(copied)
print(copied is original)
print(copied == original)
original[0].append(["canines"])
#original.append(["canines"])
#original[0].append("canines")
print(original)
print("-------- Now look at the copied version -----------")
print(copied)

# (nested iteration is a way to avoid the aliasing problem above)
# Example 1
L = ['SE','ML', 'AI', '2020', ['Python', 'JSON', 'SQL',['Gifted','Open Door',['To', 'the', 'Glory', 'of', 'God']]]]
#  4 levels, a b c d, and 4 lists L1,L2,L3,L4
L1 = []
for a in L: # first level
    L2 = []
    for b in a:
        L3 = []
        for c in b:
            L4 = []
            for d in c:
                L4.append(d)
            L3.append(c)
        L2.append(b)
    L1.append(a)
L[2] = 'DL'
L.append('AI')
L[4][3][0] = 'Supergifted'
print('Original List..: ',L)
print('Copied List....: ',L1)
# So assuming that you don’t want to have aliased lists inside of your nested list, then you’ll need to perform nested iteration.
# Example 2
original = [['dogs', 'puppies'], ['cats', "kittens"]]   # once upon a time, there was a list called original
copied_outer = []                                  # a new copied_outer_list initialised
for inner in original:                             # loop through the original list
    copied_inner = []                                  # a new copied_inner_list initialised
    for item in inner:                                 # loop through the inner_list
        copied_inner.append(item)                          # add elements of inner_list to copied_inner_list
    copied_outer.append(copied_inner)             # add elements of copied_inner_list to copied_outer_list
print('copied_inner_list: ', copied_outer)
original[0].append(["canines"])                         # add new list ["canines"] to first sublist['dogs', 'puppies']
print('orginal: ',original)
print("-------- Now look at the copied version -----------")
print('copied_inner_list: ',copied_outer)

# Or, equivalently, you could take advantage of the slice operator to do the copying of the inner list.
# Example 3
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
'''
This process above works fine when there are only two layers or levels in a nested list. However, if we want to make a 
copy of a nested list that has more than two levels, then we recommend using the copy module. In the copy module there is 
a method called deepcopy that will take care of the operation for you.
'''
# Example 4 slicing on 4 levels using the copy module
import copy
L = ['SE','ML', 'AI', '2020', ['Python', 'JSON', 'SQL',['Gifted','Open Door',['To', 'the', 'Glory', 'of', 'God']]]]
print('Control........:', L)
L_shallow = L[:]
L_deep = copy.deepcopy(L)

L[2] = 'DL'
L.append('AI')
L[4][3][0] = 'Supergifted'
L[4][0] = 'Python3'
L[4].append('Cloud')
print('Original List..: ', L)
print('ShallowCopy....: ', L_shallow)
print('DeepCopy.......:', L_deep)

# Example 5
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)

original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

# 17.7. 👩‍💻 Extracting from Nested Data

#--------------------------------Exercises----------------------------------------------

# 1. The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]

# 2. Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values.
# See comments for further instructions.
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
if 'yellow' in lst[2]:
    yellow = True
else:
    yellow = False
#Test to see if 4 is in the second list of lst. Save to variable ``four``
if 4 in lst[1]:
    four = True
else:
    four = False
#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
if 'orange' in lst[0]:
    orange = True
else:
    orange = False

# 3. Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values -
# see the ActiveCode window for further directions.
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]
# Test if 'hola' is in the list L. Save to variable name test1
if 'hola' in L:
    test1 = True
else:
    test1 = False
# Test if [5, 8, 7] is in the list L. Save to variable name test2
if [5,8,7] in L:
    test2 = True
else:
    test2 = False
# Test if 6.6 is in the third element of list L. Save to variable name test3
if 6.6 in L[2]:
    test3 = True
else:
    test3 = False

# 4. Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}
# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested.keys():
    data = True
else:
    data = False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
if 24 in nested.values():
    twentyfour = True
else:
    twentyfour = False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole' not in nested.values():
    whole = False
else:
    whole = True
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if 'physics' in nested.keys():
    physics = True
else:
    physics = False

# 5. The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = nested_d['London']['Great Britain']

# 6. Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}
# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][3]

# 7. Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []
US_count.append(nested_d['Beijing']['USA'])
US_count.append(nested_d['London']['USA'])
US_count.append(nested_d['Rio']['USA'])
print(US_count)

# 8. Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for a in l_of_l:
    third.append(a[2])
print(third)
# alternatively using list comprehension
third = [a[2] for a in l_of_l]

# 9. Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for a in athletes:
    for b in a:
        if 't' in b:
            t.append(b)
        else:
            other.append(b)
print(t, other)

# Data Collection and Processing (Week 2) -------------------------------------------

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

# Data Collection and Processing (Week 3) -------------------------------------------

# 24. Internet APIs: write computer programs that access data,  process the data in useful ways,
# even from multiple sources

# 24.6.1. Fetching in python with requests.get
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
#page = requests.get("https://presence.com.ng/index.php/blog")
print(type(page))
print(page.text[:150]) # print the first 150 characters
#print(page.text) # print whole page
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

# Make a HEAD request to a web page, and return the HTTP headers:
import requests
#the required first parameter of the 'head' method is the 'url':
#x = requests.head('https://www.w3schools.com/python/demopage.php')
x = requests.head('https://presence.com.ng/index.php/blog')
#print the response headers (the HTTP headers of the requested file):
print(x.headers)

import requests
d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)
'''
The get function in the requests module takes an optional parameter called params. If a value is specified for that 
parameter, it should be a dictionary. The keys and values in that dictionary are used to append something to the URL 
that is requested from the remote site.
'''

'''
an executable sample, using the optional params parameter of requests.get. It gets the same data from the datamus api 
that we saw previously. Here, however, the full url is built inside the call to requests.get; we can see what url was 
built by printing it out, on line 5.
'''
import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched

# requests-6-1: How would you request the URL http://bar.com/goodstuff?greet=hi+there&frosted=no
# using the requests module?
requests.get("http://bar.com/goodstuff", params = {'greet': 'hi there', 'frosted':'no'})
# note: The ? and & are added automatically, and the space in hi there is automatically encoded as %3A.

# requests-6-2: If resp is a Response object returned by a call to requests.get(),
# write some ways to extract the contents into a python dictionary or list?
'''
A. resp.json()
B. json.loads(resp.text)
'''

#--------------------Runestone textbook special function---------------------------------#
import requests
# it's not found in the permanent cache
res = requests.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
#------------------------------------------------------------------------------------------

# Using REST APIs

# Fetching a Page Google
import requests
d = {'q': 'bobby and chisom', 'tbm':'isch'}
results = requests.get('https://google.com/search', params = d)
print(results.url)
print(results.text)

# Fetching a Page Yandex
import requests
d = {'q': 'bobby and chisom', 'tbm':'isch'}
results = requests.get('https://yandex.com/search', params = d)
print(results.url)
print(results.text)

# Fetching a Page Duckduckgo
import requests
d = {'q': 'bobby and chisom', 'tbm':'isch'}
results = requests.get('https://duckduckgo.com/search', params = d)
print(results.url)
print(results.text)

# 24.8.2. Defining a function to make repeated invocations
'''
Suppose you were writing a computer program that was going to automatically translate paragraphs of text into 
paragraphs with similar meanings but with more rhymes. You would want to contact the datamuse API repeatedly, 
passing different values associated with the key rel_rhy. Let’s make a python function to do that. 
You can think of it as a wrapper for the call to requests.get.
'''
# import statements for necessary Python modules
import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    #return resp.json() # Return a python object (a list of dictionaries in this case)
print(get_rhymes("funny"))
print(get_rhymes("dash"))

# Challenge: try using the datamuse API to actually make a paragraph translator!
#_--------------------------------------------------------------------------------------------------------------------
# requests-8-1: Why would you define a function in order to make a request to a REST API for data?
# -> Because that means you have to write less repeated code if you want to make a request to the same API more than
#     once in the same program.
# -> Writing functions to complete a complex process in your code makes it easier to read and easier to fix later.
# -> Because a lot of things stay the same among different requests to the same API.
#--------------------------------------------------------------------------------------------------------------------
# requests-8-1: If the results you are getting back from a call to requests.get() are not what you expected,
# what’s the first thing you should do?
# -> look at the first few characters of the .text attribute of the Response object

# requests-8-2: In a full python environment, if there is a runtime error and you don’t get a Response object back
# from the call to requests.get(), what should you do?
# -> invoke the requestURL() function with the same parameters you used to invoke requests.get()

# requests-8-3: In the runestone environment, if there is a runtime error and you don’t get a Response object back from
# the call to requests.get(), what should you do?
# -> look at the values you passed in to requests.get()
'''
Generally, a runtime error when you invoke ``requests.get`` in the Runestone environment is caused by the value of the
 ``params`` parameter not being a dictionary, or not having only strings as keys and values.
'''

#  make a request to the iTunes API
import requests
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters,permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)

# using  Understand. Extract. Repeat. . For example, to print out the names of all the podcasts returned 
import requests
import json

parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters, permanent_cache_file="itunes_cache.txt")

py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])

# Below is some code that queries the flickr API for images that have a particular tag.
# import statements
import requests_with_caching
import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")
# Some code to open up a few photos that are tagged with the mountains and river tags...
photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)

# requests-11-1: If you wanted to search for photos tagged with either river or mountains, rather than requiring both,
# what would you change in the code? (Hint: check the documentation)
# -> tag_mode (Optional)
# Either 'any' for an OR combination of tags, or 'all' for an AND combination. Defaults to 'any' if not specified.

# requests-12-1: When you have non-ASCII characters in a string and you get an error trying to write them, which
# method should you invoke on the string?
# -> encode()
#   It's a little counter-intuitive, since it seems like you already have an encoding of the information, but you have to
#   re-encode it by substituting sequences of ASCII characters for some of the Unicode characters

# requests-12-2: In the textbook environment, what should you do if you are unable to write data to a file
# because of a Unicode encoding error?
