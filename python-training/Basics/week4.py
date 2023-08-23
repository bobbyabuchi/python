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

Method 2
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