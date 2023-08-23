"""
Sorting
how to sort python objects - both the basics and more advanced forms of sorting for dictionaries and how to break a tie (if that occurs).
The final course assessment will be a project that asks you to read fake, auto-generated data from a social media site
to analyze social media post sentiments. You will submit a csv file as well as images of graphs that demonstrate your findings.
"""
# 16.1. Introduction: Sorting with Sort and Sorted

L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]

L1.sort()
print(L1)
L2.sort()
print(L2)
# sort method returns the value None. But modifies/mutates the original list itself
# This kind of operation that works by having a side effect on the list can be quite confusing.

# sorted does not change the original list. Instead, it returns a new list.
L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2) # unchanged

print("----")

L2.sort()
print(L2)
print(L2.sort())  #return value is None

# 16.2. Optional reverse parameter

L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))
# The sorted function takes some optional parameters (see the Optional Parameters page). The first optional parameter is a key function, which will be described in the next section. The second optional parameter is a Boolean value which determines whether to sort the items in reverse order. By default, it is False, but if you set it to True, the list will be sorted in reverse order.

# 16.3. Optional key parameter

# For example, suppose you want to sort a list of numbers based on their absolute value, so that -4 comes after 3?
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))

# Now, we can pass the absolute function to sorted in order to specify that we want the items sorted in order of their absolute value, rather than in order of their actual value.
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))

# To illustrate that the absolute function is invoked once on each item, during the execution of sorted, I have added some print statements into the code.
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("Calculating the absolute value of " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Done! Here is the result, sorted based on their absolute values.")
print(L2)
# Note that this code never explicitly calls the absolute function at all. It passes the absolute function as a parameter value to the sorted function. Inside the sorted function, whose code we haven’t seen, that function gets invoked.

# Note
#
# It is a little confusing that we are reusing the word key so many times. The name of the optional parameter is 'key'. We will usually pass a parameter value using the keyword parameter passing mechanism. When we write 'key=some_function' in the function invocation, the word key is there because it is the name of the parameter, specified in the definition of the sort function, not because we are using keyword-based parameter passing.

#  You will be sorting the following list by each element’s second letter, a to z. Create a function to use when
#  sorting, called second_let. It will take a string as input and return the second letter of that string.
#  Then sort the list, create a variable called sorted_by_second_let and assign the sorted list to it. Do not use lambda.

b = "nano"
print(b[1])

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(a):
    print("Sorting " + str(a) + ' by second letter...')
    #for each_i in a:
    return a[1]
sorted_by_second_let = sorted(ex_lst, key=second_let)
print(sorted_by_second_let)

#  Below, we have provided a list of strings called nums. Write a function called last_char that takes a string as
#  input, and returns only its last character. Use this function to sort the list nums by the last digit of
#  each number, from highest to lowest, and save this as a new list called nums_sorted.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(a):
    print("Sorting " + str(a) + ' by last letter...')
    return a[-1]

nums_sorted = sorted(nums, key=last_char, reverse=True)

# Once again, sort the list nums based on the last digit of each number from highest to lowest. However,
# now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, key=lambda a: a[-1], reverse=True)
print(nums_sorted_lambda)

# 16.4. Sorting a Dictionary

#  the following code counts the frequencies of different numbers in the list.
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:              # if the key already exist,
        d[x] = d[x] + 1     # increment the value by 1
        #d[x] += 1          # increment the value by 1
    else:
        d[x] = 1            # add the key and set the value as 1
for x in d.keys():
    print("{} appears {} times".format(x, d[x]))

d = {}
d['A'] = 1
d['B'] = 2
d['A'] = d['A'] + 1
d['A'] += 1
print(d)

# we might prefer to get the outputs sorted based on the count rather than based on the items.
# we’ve named the parameter in tha lambda expression k. The property of key k that is supposed to be returned
# is its associated value in the dictionary. Hence, we have the lambda expression lambda k: d[k].
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))

"""
With a dictionary that’s maintaining counts or some other kind of score, we might prefer to get the outputs sorted 
based on the count rather than based on the items. The standard way to do that in python is to sort based on a 
property of the key, in particular its value in the dictionary. Here things get a little confusing because we have 
two different meaning of the word “key”. One meaning is a key in a dictionary. The other meaning is the parameter 
name for the function that you pass into the sorted function. Remember that the key function always takes as input 
one item from the sequence and returns a property of the item. In our case, the items to be sorted are the 
dictionary’s keys, so each item is one key from the dictionary. To remind ourselves of that, we’ve named 
the parameter in tha lambda expression k. The property of key k that is supposed to be returned is its associated 
value in the dictionary. Hence, we have the lambda expression lambda k: d[k].
"""
#  using a named function
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k):
    return d[k]

y =(sorted(d.keys(), key=g, reverse=True))

# now loop through the keys
for k in y:
    print("{} appears {} times".format(k, d[k]))

# An experienced programmer would probably not even separate out the sorting step. And they might take advantage
# of the fact that when you pass a dictionary to something that is expecting a list, its the same as passing the
# list of keys.
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

# now loop through the sorted keys
for k in sorted(d.keys(), key=lambda k: d[k], reverse=True):
#for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))

# Eventually, you will be able to read code like that and immediately know what it’s doing. For now, when you come
# across something confusing, like line 11, try breaking it down. The function sorted is invoked. Its first parameter
# value is a dictionary, which really means the keys of the dictionary. The second parameter, the key function,
# decorates the dictionary key with a post-it note containing that key’s value in dictionary d. The last parameter,
# True, says to sort in reverse order.
#
# There is another way to sort dictionaries, by calling .items() to extract a sequence of (key, value) tuples, and
# then sorting that sequence of tuples. But it’s better to learn the pythonic way of doing it, sorting the
# dictionary keys using a key function that takes one key as input and looks up the value in the dictionary.

# sort-4-1: Which of the following will sort the keys of d in ascending order of their values (i.e., from lowest to highest)?
L = [4, 5, 1, 0, 3, 8, 8, 2, 1, 0, 3, 3, 4, 3]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

def g(k, d):
    return d[k]

ks = d.keys()

# two answers
sorted(ks, key=lambda x: g(x, d))   # The lambda function takes just one parameter, and calls g with two parameters
sorted(ks, key=lambda x: d[x])      # The lambda function looks up the value of x in d.

# Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to
# the variable sorted_keys.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
d = dictionary
sorted_keys = sorted(d, key=d.get, reverse=True)
print(sorted_keys)

# 16.5. Breaking Ties: Second Sorting
# What happens when two items are “tied” in the sort order? For example, suppose we sort a list of words
# by their lengths. Which five letter word will appear first?

# how python sorts tuples
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]
for tup in sorted(tups):
    print(tup)

# In the code below, we are going to sort a list of fruit words first by their length, smallest to largest, and then
# alphabetically to break ties among words of the same length. To do that, we have the key function return a tuple
# whose first element is the length of the fruit’s name, and second element is the fruit name itself.
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
print(new_order)
for fruit in new_order:
    print(fruit)

# Here, each word is evaluated first on it’s length, then by its alphabetical order. Note that we could continue to
# specify other conditions by including more elements in the tuple.
#
# What would happen though if we wanted to sort it by largest to smallest, and then by alphabetical order?
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
for fruit in new_order:
    print(fruit)
"""
Do you see a problem here? Not only does it sort the words from largest to smallest, but also in reverse alphabetical 
order! Can you think of any ways you can solve this issue?
- One solution is to add a negative sign in front of len(fruit_name), which will convert all positive numbers to 
negative, and all negative numbers to positive. As a result, the longest elements would be first and the shortest 
elements would be last.
"""
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# We can use this for any numerical value that we want to sort, however this will not work for strings
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
# A. first city name (alphabetically), then temperature (lowest to highest)

# What how will the following data be sorted?
weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
# answer is => first city name (reverse alphabetically), then temperature (lowest to highest)
# In this case, the reverse parameter will cause the city name to be sorted reverse alphabetically instead of
# alphabetically, and it will also negate the negative sign in front of the temperature.

# 16.6. 👩‍💻 When to use a Lambda Expression
"""
Though you can often use a lambda expression or a named function interchangeably when sorting, it’s generally best 
to use lambda expressions until the process is too complicated, and then a function should be used. For example, 
in the following examples, we’ll be sorting a dictionary’s keys by properties of its values. Each key is a state 
name and each value is a list of city names.
- For our first sort order, we want to sort the states in order by the length of the first city name. Here, it’s pretty 
easy to compute that property. states[state] is the list of cities associated with a particular state. So If state 
is a list of city strings, len(states[state][0]) is the length of the first city name. Thus, we can use a 
lambda expression:
"""
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))

"""
That’s already pushing the limits of complex a lambda expression can be before it’s reall hard to read (or debug).

- For our second sort order, the property we want to sort by is the number of cities that begin with the letter ‘S’. 
The function defining this property is harder to express, requiring a filter and count accumulation pattern. 
So we are better off defining a separate, named function. Here, we’ve chosen to make a lambda expression that looks 
up the value associated with the particular state and pass that value to the named function s_cities_count. 
We could have passed just the key, but then the function would have to look up the value, and it would be a little 
confusing, from the code, to figure out what dictionary the key is supposed to be looked up in. Here, 
we’ve done the lookup right in the lambda expression, which makes it a little bit clearer that we’re just sorting 
the keys of the states dictionary based on a property of their values. It also makes it easier to reuse the 
counting function on other city lists, even if they aren’t embedded in that particular states dictionary.
"""
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names
# so they appear alphabetically. Save this list to the variable alphabetical.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
m = medals
k = m.keys()
alphabetical = sorted(k)
print(alphabetical)

# Given the same dictionary, medals, now sort by the medal count. Save the three countries with
# the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
m = medals
top_three = sorted(m, key=m.get, reverse=True)[:3]
print(top_three)

# Sort the following list by each element’s second letter a to z. Do so by using lambda.
# Assign the resulting value to the variable lambda_sort.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda x: x[1])
print(lambda_sort)

# Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function.
# Save this sorted list in the variable sorted_id.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda x: str(x)[-4:])

# Create a function called last_four that takes in an ID number and returns the last four digits. For example,
# the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the
# variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint:
# Remember that only strings can be indexed, so conversions may be needed.
def last_four(x):
    return (str(x)[-4:])

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

last_four(ids)
sorted_ids = sorted(ids, key=last_four)
print(sorted_ids)