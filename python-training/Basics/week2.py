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

