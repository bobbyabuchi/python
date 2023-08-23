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