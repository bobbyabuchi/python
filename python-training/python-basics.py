# PYTHON BASICS Week 1 --------------------------------------------------------

fruit = "Banana"
x = len(fruit)
print (x)

lastChar = fruit[-1]
print (lastChar)

lastChar2 = fruit[x-1]
# [5-1] = [4] print(fruit[4])
print(lastChar2)

fruit = "Banana"
x = len(fruit)
print (x)

lastChar = fruit[-1]
print (lastChar)

lastChar2 = fruit[x-1]
# [5-1] = [4] print(fruit[4])
print(lastChar2)

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[:])

# Create a new list using the 9th through 12th elements (four items in all) of *new_lst* and assign it to the variable *sub_lst*.
new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst [8:12]
print(sub_lst)

# Create a new list of the 6th through 13th elements of *lst* (eight items in all) and assign it to the variable *output*.
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
output = lst[5:13]
print(output)

# Create a variable output and assign it to a list whose elements are the words in the string str1.
str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print (output)

# Write a program that extracts the last three items in the list sports and assigns it to the variable last.
# Make sure to write your code so that it works no matter how many items are in the list.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:]
print(last)

# Write code that combines the following variables
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
s = " "
message = by + s + az + io + s + qy
print(message)

# python is a zero-index based language and slices are inclusive of the first index and exclusive of the second.
ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

# what is the type of 'm' and 'n'?
l = ['w', '7', 0, 9]
m = l[1:2]
n = l[1]
print(type(m))
# reason: a slice returns a list no matter how large the slice.
print(type(n))
# reason: the quotes around the number mean that this is a string.

# what type is x?
b = "My, what a lovely day"
x = b.split(',')
print(type(x), x)

# what type is a?
b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
print(type(a), a)
# note: the string is split into a list, then joined back into a string,
# then split again, and finally joined back into a string.

# for the moment we’ll just print a message for each friend.
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")

# sequence iteration: iteration by item
for loopVar in "Go Spot Go":
    print(loopVar)

achar = "Go Spot God"
print(achar)

string1 = "python rocks"
for loopVar in string1: # for each item in the string, print "HELLO"
   print("HELLO")

#
string1 = "python rocks"
for loopVar in string1[3:8]:
   print("HELLO")

# Iteration Simplifies our Turtle Program
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:      # repeat four times
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()

#----------------------------RANGE------------------------------------------------------------
print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

# The variable accum will be reset to 0 each time through the loop.
# Then it will add the current item. Only the last item will count.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
   accum = 0
   accum = accum + w
print(accum)

# PYTHON BASICS Week 2 --------------------------------------------------------

#----------------------------RANGE------------------------------------------------------------
print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

# The variable accum will be reset to 0 each time through the loop.
# Then it will add the current item. Only the last item will count.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for eachItem in nums:
   accum = 0
   accum = accum + eachItem
print(accum)

#-----------------------

# Create a list of int 0-52 and assign to a variable 'numbers'
numbers = range(0, 53)
print(list(numbers)) # casting the range() as a list using list()

#---------------------------------------------------------------------------------------------------------------

# Count the number of characters in a string without using the len()

# Example 1
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
count = 0
for c in str1:
    count = count + 1
print("Total number of characters : ", count)

# Example 2
str1 = "Promoting excellence in life and career through education, applicable research and technologic innovation."
numbs = list(str1) # casted as a list here
accum = 0
for lopVar in numbs:
    accum = accum + 1
print(accum)

#---------------------------------------------------------------------------------------------------------------------

# Create a list of numbers 0 through 40 and assign this list to the variable numbers.
# Then, accumulate the total of the list’s values and assign that sum to the variable sum1.
numbers = range(0,41)
sum1 = 0
for w in numbers:
    sum1 = sum1 + w
print(sum1)

#--------------LISTs in Python--------------------
 abc = ["a","b","c","d"]
 print(abc)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:5])
for eachElemt in thislist:
    print(eachElemt)
# -----------------------------------------------------------
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(5):
    print(n, fruits[n])

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

s = "python"
for idx in range(len(s)):
   print(s[idx % 2])


#---------------------------------------------------------------------------
grocery_item = ""
while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list simply type: done")
    print(grocery_item)
print

grocery_item = ""
grocery_list = []
while grocery_item != "done":
    grocery_item = input("Add items to your grocery list. And simply type 'done' to stop adding")
    if grocery_item == 'done':
        continue
    else:
        print("adding the item to the list")
        grocery_list.append(grocery_item)
print("Here is our grocery list:")
print(grocery_list)

for i in range(5):
    print(i)


#------------------------------------------------------------------------------
# addition_str is a string with a list of numbers separated by the + sign.
# Write code that uses the accumulation pattern to take the sum of all of the numbers and
# assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int()
# to cast to an integer).

addition_str = "2+5+10+20"
print(addition_str, "as it were")
addition_str = addition_str.split("+")
print(addition_str, "after .split('+')")
addition_str = [int(eachItem) for eachItem in addition_str]
print(addition_str, "after int()")
sum_val = 0
for eachItem in addition_str:
    sum_val = sum_val + eachItem
print(sum_val, "is final answer")

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
week_temps_f = [float(eachItem) for eachItem in week_temps_f]
count = 0
for eachInt in week_temps_f:
    count = count + eachInt
    print(count)
print(week_temps_f)
#print(count)
avg_temp = count/len(week_temps_f)
print(avg_temp)

#------------tough question----------------------
# Write code to create a list of word lengths for the words in original_str
# using the accumulation pattern and assign the answer to a variable num_words_list.
# (You should use the len function).
original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = original_str.split(" ")
num_words_list = [len(eachWord) for eachWord in num_words_list]
print(num_words_list)

# PYTHON BASICS Week 3 --------------------------------------------------------

# 8.1. Intro: What we can do with Turtles and Conditionals

import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Pink")
amy.forward(50)
if amy.pencolor() == "Pink":
    amy.right(60)
    amy.forward(100)
else:
    amy.left(60)
    amy.forward(100)

kenji = turtle.Turtle()
kenji.forward(60)
if kenji.pencolor() == "Pink":
    kenji.right(60)
    kenji.forward(100)
else:
    kenji.left(60)
    kenji.forward(100)

#----------------------------------------------

import turtle
wn = turtle.Screen()

amy = turtle.Turtle()
amy.pencolor("Pink")
amy.right(170)

colors = ["Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Orange", "Pink", "Pink", "Orange", "Yellow", "Purple", "Orange", "Purple", "Yellow", "Orange", "Pink", "Orange", "Purple", "Purple", "Yellow", "Orange", "Pink", "Orange", "Yellow", "Purple", "Yellow"]


for color in colors:
    if amy.pencolor() == "Purple":
        amy.forward(50)
        amy.right(59)
    elif amy.pencolor() == "Yellow":
        amy.forward(65)
        amy.left(98)
    elif amy.pencolor() == "Orange":
        amy.forward(30)
        amy.left(60)
    elif amy.pencolor() == "Pink":
        amy.forward(50)
        amy.right(57)

    amy.pencolor(color)

print(5 == 5)

#------------------------------------------------------

x = 102
y = 10

if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x and y must be equal")
print("x and y must be equal")

#------------------------------------------------------
#---Create one conditional to find whether “false” is in string str1...
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
output = "False. You aren't you?"
if 'false' in str1:
    print(output)
elif "true" in str1:
    output = "True! You are you!"
    print(output)
else:
    output = "Neither true nor false!"
    print(output)

#Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.
percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for eachTemp in percent_rain:
    if eachTemp > 90:
        resps.append('Bring an umbrella.')
    elif eachTemp > 80:
        resps.append('Good for the flowers?')
    elif eachTemp > 50:
        resps.append('Watch out for clouds!')
    else:
        resps.append('Nice day!')

# We have created conditionals for you to use. Do not change the provided conditional statements.
# Find an integer value for x that will cause output to hold the values True and None.
# (Drawing diagrams or flow charts for yourself may help!)
x =
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)

#Sometimes when we’re accumulating, we don’t want to add to our accumulator every time we iterate.
# Consider, for example, the following program which counts the number of letters in a phrase.
phrase = "What a wonderful day to program"
tot = 0
for char in phrase:
    if char != " ":
        tot = tot + 1
print(tot)

# We can use conditionals to also count if particular items are in a string or list.
# The following code finds all occurrences of vowels in the following string.
s = "what if we went to the zoo"
x = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        x += 1
print(x)

# Accumulating the Max Value
# The following example shows how we can get the maximum value from a list of integers.

# For each string in the list words, find the number of characters in the string. If the number of characters in the string is greater than 3, add 1 to the variable num_words so that num_words should end up with the total number of words with more than 3 characters.
words = ["water", "chair", "pen", "basket", "hi", "car"]
# no of chars in each string in the list
# if no of char is > 3, add 1
for eachWord in words:
    num_words = len(eachWord)
    if num_words > 3:
        #print("Hi")
        num_words = num_words + 1
    print(num_words)

# Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense.
# Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for eachWord in words:
    if 'e' in eachWord[-1]:
        past_tense.append(eachWord+'d')
    else:
        past_tense.append(eachWord+'ed')
print(past_tense)

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi_split = rainfall_mi.split(",")
num_rainy_months = 0
for x in rainfall_mi_split:
    x = float(x)
    if x > 3.0:
        num_rainy_months += 1
print(num_rainy_months)

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi = rainfall_mi.split(",")
num_rainy_months = 0
for eachAvg in rainfall_mi:
    eachAvg  = float(eachAvg)
    if eachAvg > 3.0:
        num_rainy_months = num_rainy_months + 1
        # or num_rainy_months += 1
print(num_rainy_months)

# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Solution
sentence = sentence.split(' ')
same_letter_count = 0
for eachWord in sentence:
    if eachWord[0] == eachWord[-1]:
        same_letter_count = same_letter_count + 1
print(same_letter_count)


# Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
#
# HINT 1: Use the accumulation pattern!
#
# HINT 2: the in operator checks whether a substring is present in a string.
#
# Hard-coded answers will receive no credit.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for eachItem in items:
    if 'w' in eachItem:
        acc_num = acc_num + 1
print(acc_num)

# Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = sum([1 for eachWord in s if eachWord in vowels])
print(num_vowels)

# PYTHON BASICS Week 4 --------------------------------------------------------

"""
WEEK FOUR - SEQUENCE MUTATION
"""
# -> methods("string") leave do not alter original string, but return new one
# -> list is a datatype, is mutable *mutating methods on list return None*

fruit = ["banana", "apple", "cherry"] # create a list, set in variable fruits
print(fruit)

fruit[0] = "pear" # reassign/change and item in postion '0'
fruit[-1] = "orange" # reassign/change and item in postion '1'
print(fruit)

# By combining assignment with the slice operator we can update several elements at once.
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y'] # target and change items in position 1-3 [...,b, c,...] with [x, y]
print(alist)

# 9.3. List Element Deletion
# Using slices to delete list elements can be awkward and therefore error-prone.
# Python provides an alternative that is more readable. The del statement removes an element from a list by using its position.

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(id(alist))

# remove elements from a list by assigning the empty list to them.
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

# insert elements into a list by squeezing them into an empty slice at the desired location.
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

# Strings are immutable, which means you cannot change an existing string.
# The best you can do is create a new string that is a variation on the original.
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)  # same as it was

# concatenate a new first letter onto a slice of greeting
phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
e = excited_phrase_complete = phrase_complete[:-1] + "!"
print(e)

alist = [4,2,8,6,5]
alist[2] = True
print(alist)

# 9.4. Objects and References, [note an object is something a variable can refer to]
a = "banana" # no variation in string ID, so a is b
b = "banana" # no variation in string ID, and b is a
c = ['b','a','n','a','n','a'] # there is a variation in list IDs so c is not d
d = ['b','a','n','a','n','a'] # there is a variation in list IDs so d is not c
print (a==b)
print(a is b)
print (c == d)
print (c is d)
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))

# 9.5. Aliasing -> Since variables refer to objects, if we assign one variable to another,
# both variables refer to the same object: Because the same list has two different names, a and b,
# we say that it is aliased. Changes made with one alias affect the other.

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

# MOTE: Although this behavior can be useful, it is sometimes unexpected or undesirable. In general,
# it is safer to avoid aliasing when you are working with mutable objects.

alist = [4,2,8,6,5]
blist = alist
blist[3] = 999
print(alist) # ->  [4,2,8,999,5]

# 9.6. Cloning Lists
# If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself,
# not just the reference. This process is sometimes called cloning, to avoid the ambiguity of the word copy.
# The easiest way to clone a list is to use the slice operator.

a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)

b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)
print(b)

# Yes, when we are using the remove method, we are just editing the existing list, not making a new copy.
lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]
print(lst)

#  the behavior of obj = obj + object_two is different than obj += object_two when obj is a list.
#  The first version makes a new object entirely and reassigns to obj.
#  The second version changes the original object so that the contents of object_two are added to the end of the first.
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']

# more like CONVERT STRING TO A LIST HERE
sent = "The mall has excellent sales right now."
wrds = sent.split()
print(wrds)

# 9.7. Mutating Methods
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

mylist = [1,2,3,4,3]
mylist.count(2)
print(mylist)
mylist.insert(3, 5)
print(mylist)
print(mylist.index(3))
print(mylist.count(3))

# 9.8. Append versus Concatenate
origlist = [45,32,88]

origlist.append("cat")
print(origlist)

st = "Warmth"
a = []
a.append(st)
a.append("Cozy")
a.append("Juicy")
print(a)

#  character by character, you can add to the empty list.
#  The process looks different if you concatentate as compared to using append.
st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)

st = "Warmth"
a = []
a.append(st[0])
a.append(st[1])
a.append(st[2])
a.append(st[3])
a.append(st[4])
a.append(st[5])
print(a)

alist = [4,2,8,6,5]
#alist = alist + 999 # Error, you cannot concatenate a list with an integer.
alist + [999] # in order to perform concatenation you must have two lists.
print(alist)

# 9.9. Non-mutating Methods on Strings
ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

# Returns the leftmost index where the substring item is found and causes a runtime error if item is not found
strg1 = "Bobby"
strg2 = "bobby"
print(strg1.index("b"))
print(strg2.index("b"))

# Returns a string with the leading and trailing whitespace removed
strg3 = "   What shall I more   say   "
print(strg3)
print(strg3.strip())

# Replaces all occurrences of old substring with new
strg4 = "Bobby"
print(strg4.replace("B", "13"))
strg4 = strg4.replace("B","13")
strg4 = strg4.replace("bb","66")
print(strg4)

# s[1] is y and the index of n is 5, so 5 y characters.
# It is important to realize that the index method has precedence over the repetition operator.
# Repetition is done last.
s = "python rocks"
print(s[1]*s.index("n"))

# 9.9.1. String Format Method
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))

# in a more readable way...
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))

# The string method format, makes substitutions into places in a string enclosed in braces
person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)
# a more concise version:
person = input('Enter your name: ')
print('Hello {}!'.format(person))

#...There can be multiple substitutions, with data of any type. Next we use floats.
# Try original price $2.50 with a 7% discount:
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

# Format strings can give further information inside the braces showing how to specially format data.
# For two decimal places, put :.2f inside the braces for the monetary values:
origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

"""
A technical point: Since braces have special meaning in a format string, 
there must be a special rule if you want braces to actually be included in the final formatted string. 
The rule is to double the braces: \{\{ and \}\}.
"""
# For example mathematical set notation uses braces.
# The initial and final doubled braces in the format string below generate literal braces in the formatted string:
a = 5
b = 9
setStr = 'The set is \{\{\{}, {}}}.'.format(a, b)
print(setStr)

x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))

v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))

# It is important to remember that methods like append, sort, and reverse all return None.
# They change the list; they don’t produce a new list.
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = winners.reverse()
print(z_winners) # this will return None

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = winners
z_winners.reverse()
print(z_winners) # this can now give me the reverse

name = "Bobby"
new_name = name.upper()
print(new_name) # while this will return a value for string...

nameList = ['Bobby', 'Wordfire']
new_nameList = nameList.upper() # ...this will give an error
new_nameList = nameList.reverse() # and this will return None
print(new_nameList)

# 9.10. The Accumulator Pattern with Lists
# accumulate values into a list...the following program which transforms a list into a new list by squaring each of the values.
nums = [3, 5, 8]
accum = []              # initialize the accumulator variable
for w in nums:          # iterate through the sequence
    x = w**2            #...(squaring each iterable)
    accum.append(x)     # update step appends the new item to the list which is stored in the accumulator variable
print(accum)
"""
Note: in the example above, we could have written: 
    accum = accum + [x], or 
    accum += [x]. 
In either case, we’d need to concatenate a list containing x, not just x itself.
"""

lst= [3,0,9,4,1,7]
k = range(len(lst)) # = 012345, = 5
print(k)
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)

name = "Bob"
name = name + "by"
print(name)

# For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"] # a list
ing = []                    # initialize empty list
for eachWord in verbs:      # iterate through the sequence
    x = eachWord + "ing"    # (concatenate 'ing' to each item in the sequence)
    ing.append(x)           # update
print(ing)

# another example
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for wrd in wrds:
    add_ed = wrd + "ed"
    past_wrds.append(add_ed)
print(past_wrds)

# Accumulator Pattern with Lists and conditionals
aList = ['Ball','Love']
nList = []
for z in aList:
    if 'e' in z:
        y = z + 'r'
    else:
        y = z + 'er'
    nList.append(y)
print(nList)

numbs = [5, 10, 15, 20, 25]
k = []
for i in numbs:
    j = i + 5
    k.append(j)
print(k)

# 9.11. The Accumulator Pattern with Strings

# accumulate strings

s = input("Enter some text")
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"

print(ac)

# strange order of concatenation
s = "ball"
r = ""
for item in s:
    #r = item.upper() + r # this will return "LLAB" (reversed due to the order of the concatenation)
    #r = r + item.upper() # this will return "BALL"
print(r) # will print LLAB (because the order is )

# further investigating the order of concatenation
s = "ball"
r = s.upper() + "ing"
n = "soccer" + s.upper()
print(r)
print(n)

# For each character in the string already saved in the variable str1, add each character to a list called chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for n in str1:
    chars.append(n)
print(chars)

# RANGE function
for x in range(6):
    print(x)

# using the range function
for i in range(10):
    print(i)
    # i = 5 # what does this line do?

output = ""
for i in range(35):
    output = output + "a"
print(output)

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for eachItem in str1:
    chars.append(eachItem)
print(chars)

# how to iterate through a list
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

for color in colors:
    print(color)

# accumulate a list by appending or deleting items!
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
initials = []

for color in colors:
    initials.append(color[0])

print(initials)

# print initials from names input
names = input("Enter names")
names = names.split()
initials = []
for name in names:
    initials.append(name[0])
print(initials)

#  iterate through a list and accumulate some data into it or delete data from it
# filter out all words that begin with P, B, or T.
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois", "Peach", "Beige"]

for position in range(len(colors)):
    color = colors[position]
    print(color) # print all the items in list now turned RANGE
    if color[0] in ["P", "B", "T"]:
        del colors[position]
print(colors)
"""
In the code above, we iterated through range(len(colors)) because it made it easier to locate the position of the item in the list and delete it. 
However, we run into a problem because as we delete content from the list, the list becomes shorter. 
Not only do we have an issue indexing on line 4 after a certain point, but we also skip over some strings because they’ve been moved around. 
To see this more easily, try walking through this code in codelens. 
Note that each time we iterate through the list python does not reevaluate the iterator variable.
"""

# trying to accumulate a list that we’re iterating through as well
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
for color in colors:
    if color[0] in ["A", "E", "I", "O", "U"]:
        colors.append(color)
print(colors) # will add orange before indigo on the list, why?

# FINAL REVIEW QUESTIONS

# append to a list
a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)

# accumulate the total sum of a list of numbers
nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n
print(s)

# aliasing could cause potential confusion here because
# b and z reference the same list and changes are made using both aliases.
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

# accumulate the total number of strings(!a particular data type!) in the list
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1
print(s)

# For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app = []
for n in ael:
    app.append(n)
print(app)

# FINAL REVIEW

# determine how many are 90 or above and assign that result to the value 'a_scores'
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores = scores.split()
a_scores = []
for n in scores:
    n = int(n)
    if n >= 90:
        a_scores.append(n)
a_scores = len(a_scores)

"""
Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro. 
Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and
 there should be nothing to separate the letters of the acronym. 
 Words that should not be included in the acronym are stored in the list stopwords. 
 For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.
"""
# Method 1
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org = org.split()
acro = ""
for letter in org:
    if letter.lower() not in stopwords:
        letter = letter[0].upper()
        acro += acro.join(letter)
print(acro)

# Method 2
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
stopwords = set(w.upper() for w in stopwords)
acro = ''.join(i[0] for i in org.upper().split(' ') if i not in stopwords)


# 3. Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro.
# The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space).
# Words that should not be included in the acronym are stored in the list stopwords.
# For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent = sent.split()

acro = '. '
acro = acro.join(letter[:2].upper()
for letter in sent if letter not in stopwords)
print(acro)

# Method 2
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = '. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)
print(acro)

"""
A palindrome is a phrase that, if reversed, would read the exact same. 
Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. 
Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
"""
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print (r_phrase)

"""
Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, 
how much is in stock, and how much it costs. Print out each item in the list with the same formatting, 
using the .format method (not string concatenation). For example, the first print statment should read 
The store has 12 shoes, each for 29.99 USD.
"""
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for each_item in inventory:
    name, qty, amt = each_item.split(", ")
    print("The store has {} {}, each for {} USD.".format(qty, name, amt))