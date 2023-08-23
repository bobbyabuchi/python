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