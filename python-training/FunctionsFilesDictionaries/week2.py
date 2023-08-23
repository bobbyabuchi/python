"""
Dictionaries and Dictionary Accumulation
new data type, dictionaries. You will be introduced to the mechanics of dictionaries
and then get practice using them in accumulation patterns, both to build a dictionary using the pattern
as well as find the best, or worst, result using the pattern.
"""
car_dict = {"brand": "Ford","model": "Mustang","year": 1964}
print(car_dict)
# same as...for readability and clarity
car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car_dict)

# adding items to dictionary
myDictionary = {}
myDictionary['key'] = 'value'
myDictionary['Balance'] = 20000
myDictionary['Description'] = 'Fee'
print(myDictionary)

# Accessing Items
x = car_dict["model"]
x = car_dict.get("model") # using get() method

# You can change the value of a specific item by referring to its key name:
# Change the "year" to 2018:
car_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car_dict["year"] = 2020

# Loop Through a Dictionary
car_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Print all key names in the dictionary, one by one:
for each_key in car_dict:
  print(each_key)
# Print all values in the dictionary, one by one:
for each_value in car_dict:
  print(car_dict[each_value])
# You can also use the values() function to return values of a dictionary:
for each_value in car_dict.values():
  print(each_value)
# Loop through both keys and values, by using the items() function:
for each_key, each_value in car_dict.items():
  print(each_key, each_value)
# Check if Key Exists
if "model" in car_dict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# determine how many items (key-value pairs) a dictionary has, use the len() method
print(len(car_dict))
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
car_dict["color"] = "red"
# removing items, there be several methods though...but using pop()
car_dict.pop("model")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car_dict.popitem()
# The del keyword removes the item with the specified key name:
del car_dict["model"]
# The clear() keyword empties the dictionary:
car_dict.clear()
# Make a copy of a dictionary with the copy() method:
copy_of_car_dict = car_dict.copy()
# Make a copy of a dictionary with the dict() method:
copy_car_dict = dict(car_dict)
del car_dict["model"] # removes the model key-value pair
# The del keyword can also delete/annihilates the dictionary completely:
del car_dict
# Nested Dictionaries: dictionaries within a dictionary
myPapers = {
    "paper1" : {
    "title" : "Computer Programming",
    "year" : 2004
  },
    "paper2" : {
    "title" : "Software Engineering",
    "year" : 2007
  },
    "paper3" : {
    "title" : "IT Automation",
    "year" : 2011
  },
    "paper4" : {
    "title" : "Machine Learning",
    "year" : 2011
    }
}
print(myPapers)

# if you want to nest three dictionaries that already exists as dictionaries:
paper1 = {"title" : "Computer Programming", "year":2014}
paper2 = {"title":"Software Engineering", "year":2017}
paper3 = {"title": "IT Automation", "year":2019}
paper4 = {"title":"Machine Learning", "year":2020}
allPapers = {
  "paper1" : paper1,
  "paper2" : paper2,
  "paper3" : paper3
}
print(allPapers)

# make a new dictionary with the dict() constructor
car_dict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# equals rather than colon is used for the assignment
print(car_dict)

# Python Dictionary update() Method
car = {"brand": "Ford","model": "Mustang","year": 1964}
car.update({"color": "White"})
print(car)

# Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics
# by adding 5 to the current value (Phelps will now have 28 total medals).
# Do not rewrite the dictionary.
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps'] = swimmers['Phelps'] + 5
print(swimmers)

# Spain won 2 more gold medals. Update golds to reflect this information.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
print(golds)
golds['Spain'] += 2
print(golds)

# Python Dictionary keys() Method
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
print(x) # will output the keys

inventory = {
    'apples': 430,
    'bananas': 312,
    'oranges': 525,
    'pears': 217
}
print(inventory['apples'],inventory['oranges'])
for each_key in inventory.keys():   # the order in which we get the keys is not defined
    print("Key", each_key, "maps to the value", inventory[each_key])
ks = list(inventory.keys())
print(ks)

# iterating over a dictionary implicitly iterates over its keys.
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for each_key in inventory:
    #print("Key", each_key)
    print(each_key,"is a key")

# The values and items methods are similar to keys. They return the objects which can be iterated over.
# Note that the item objects are tuples containing the key and the associated value.
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(list(inventory.values())) # converted to a list with the list()
print(list(inventory.items())) # converted to a list with the list()
for k in inventory:
    print("Key",k,"maps to",inventory[k])

# using The in and not in operators can test if a key is in the dictionary:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    if inventory['bananas'] == 0:
        print("bananas out of stock")
    else:
        print(inventory['bananas'])
else:
    print("bananas out of stock")

# The get method allows us to access the value associated with a key,

# There exists a variation of get that allows a second parameter that serves as an alternative return value
# in the case where the key is not present. This can be seen in the final example below.
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.get("apples"))
print(inventory.get("cherries")) # get will not cause a runtime error if the key is not present. It will instead return None.
print(inventory.get("cherries",0)) # In this case, since “cherries” is not a key, return 0 (instead of None).


places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
print(places)
places["Brazil"] = 2016
print(places)

# Assign to the variable events a list of the keys from the dictionary medal_events
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
print(events)

# Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point
# in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable
# belarus. Do not hardcode this.
medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
belarus = medal_count.get("Belarus")
print(belarus)

# The dictionary total_golds contains the total number of gold medals that countries have won over the
# course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number
# to the variable name chile_golds. Do not hard code this!
total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds.get("Chile")
print(chile_golds)

# Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016,
# and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing"
# to a variable fencing_value. Remember, do not hard code this.
US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals.get("Fencing")
#print(fencing_value)

# 11.6. Introduction: Accumulating Multiple Results In a Dictionary

# If we want to find out how often the letter ‘t’ occurs, we can accumulate the result in a count variable.
var_f = open('I:/pydata/scarlet.txt', 'r')
txt = var_f.read()
# now txt is one long string containing all the characters
t_count = 0                                                 # initialize the accumulator variable
for each_item in txt:                                            # loop through each characrer/item in txt
    if each_item == 't':                                            # check if any if it is equal to 't'
        t_count += 1                                                    #increment the counter
print("t: " + str(t_count) + " occurrences")

# accumulate counts for more than one character as we traverse the text.
# Suppose, for example, we wanted to compare the counts of ‘t’ and ‘s’ in the text.
var_f = open('I:/pydata/scarlet.txt', 'r')
txt = var_f.read()
# now txt is one long string containing all the characters
t_count = 0                                                 # initialize the accumulator variable
s_count = 0                                                 # initialize the accumulator variable
for each_item in txt:                                            # loop through each characrer/item in txt
    if each_item == 't':                                            # check if any if it is equal to 't'
        t_count += 1                                                    #increment the counter
    elif each_item == 's':
        s_count += 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurences")

# OK, but you can see this is going to get tedious if we try to accumulate counts for all the letters.
# We will have to initialize a lot of accumulators, and there will be a very long if..elif..elif statement.
# Using a dictionary, we can do a lot better.
#
# One dictionary can hold all of the accumulator variables. Each key in the dictionary will be one letter,
# and the corresponding value will be the count so far of how many times that letter has occurred.
var_f = open('I:/pydata/scarlet.txt', 'r')
txt = var_f.read()                                  # now txt is one long string containing all the characters
x = {}                                              # start with an empty dictionary
x['t'] = 0                                          # initialize & add the t counter to dictionary
x['s'] = 0                                          # initialize & add the s counter to dictionary
for each_item in txt:
    if each_item == 't':
        x['t'] += 1                         # increment the t counter
    elif each_item == 's':
        x['s'] += 1                         # increment the s counter
print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")

# This hasn’t really improved things yet, but look closely at lines 8-11 in the code above.
# Whichever character we’re seeing, t or s, we’re incrementing the counter for that character.
# So lines 9 and 11 could really be the same.
var_f = open('I:/pydata/scarlet.txt', 'r')
txt = var_f.read()                                  # now txt is one long string containing all the characters
x = {}                                              # start with an empty dictionary
x['t'] = 0                                          # initialize & add the t counter to dictionary
x['s'] = 0                                          # initialize & add the s counter to dictionary
for each_item in txt:
    if each_item == 't':
        x[each_item] += 1                     # increment the t counter | (using the variable each_item whose value
    elif each_item == 's':
        x[each_item] += 1                     # increment the s counter | is ‘s’ or ‘t’, or some other character)
print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")

"""
One other nice thing about using a dictionary is that we don’t have to prespecify what all the letters will be. 
In this case, we know in advance what the alphabet for English is, but later in the chapter we will count the 
occurrences of words, and we do not know in advance all the of the words that may be used. 
Rather than pre-specifying which letters to keep accumulator counts for, we can start with an empty dictionary
and add a counter to the dictionary each time we encounter a new thing that we want to start keeping count of.
"""

# We can do better still, still on the occurence code
var_f = open('I:/pydata/scarlet.txt', 'r')
txt = var_f.read()                                  # now txt is one long string containing all the characters
x = {}                                              # start with an empty dictionary
for each_item in txt:
    if each_item not in x:
        x[each_item] = 0                # we have not seen this character before, so initialize a counter for it
    x[each_item] += 1               # whether we've seen it before or not, increment its counter
print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")
print("cool")

# Instead of the print statements at the end picking out the specific keys ‘t’ and ‘s’.
# We can generalize that, too, to print out the occurrence counts for all of the characters,
# using a for loop to iterate through the keys in x, now letter_counts.
var_f = open('I:/pydata/scarlet.txt', 'r')
txt = var_f.read()  # now txt is one long string containing all the characters
letter_counts = {}  # start with an empty dictionary
for each_item in txt:
    if each_item not in letter_counts:
        letter_counts[each_item] = 0                # initialize a counter for it
    letter_counts[each_item] += 1                   # whether we've seen it before or not, increment its counter
for each_item in letter_counts.keys():
    print(each_item + ": " + str(letter_counts[each_item]) + " occurrences")

#  \\n, appears 5155 times in the text. In other words, there are 5155 lines of text in the file.
#  Let’s test that hypothesis.
f = open('I:/pydata/scarlet.txt', 'r')
txt_lines = f.readlines() # now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))
print(txt_lines[70:85])

# Split the string into a list of words, then create a dictionary that contains each word and the number of times
# it occurs. Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
sentence = sentence.split()
word_counts = {}
for each_word in sentence:
    if each_word not in word_counts:
        word_counts[each_word] = 0      # add word/key to dictionary, with initial value of zero
    word_counts[each_word] += 1         # increment it's counter/value
print(word_counts)

# Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "peter piper picked a peck of pickled peppers"
char_d = {}
stri = list(stri)
for x in stri:
    if x not in char_d:
        char_d[x] = 0
    char_d[x] += 1
print(char_d)

# 11.7. Accumulating Results From a Dictionary

# we can also iterate through the keys in a dictionary,
# accumulating a result that may depend on the values associated with each of the keys.
#
# For example, suppose that we wanted to compute a Scrabble score for the Study in Scarlet text.
# Each occurrence of the letter ‘e’ earns one point, but ‘q’ earns 10.
# We have a second dictionary, stored in the variable letter_values.
# Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in
# the counts dictionary. For each of those letters that has a letter value
# (no points for spaces, punctuation, capital letters, etc.), we add to the total score.
var_f = open('I:/pydata/scarlet2.txt', 'r')
txt = var_f.read() # now txt is one long string containing all the characters

x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        x[c] = 0    # add in dicionary and set initial value to be 0
    x[c] += 1 # increment its counter/value by 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for y in x:
    if y in letter_values:
        tot = tot + letter_values[y] * x[y]

print(tot)

# The dictionary travel contains the number of countries within each continent that Jackie has traveled to.
# Find the total number of countries that Jackie has been to, and save this number to the variable name total.
# Do not hard code this!
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for countries in travel:
    x = travel[countries]
    #int(x)
    total = total + x
print(total)

# schedule is a dictionary where a class name is a key and its value is how many credits it was worth.
# Go through and accumulate the total number of credits that have been earned so far and
# assign that to the variable total_credits. Do not hardcode.
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}
total_credits = 0
for credit_earned in schedule:
    x = schedule[credit_earned]
    #int(x)
    total_credits = total_credits + x
print(total_credits)

# 11.8. Accumulating the Best Key

# Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same
# maximum value, it’s OK to print out either one.
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

d_keys = d.keys() # get the d dictionary keys
best_key_so_far = list(d_keys)[0] # Have to turn d_keys into a real list before using [] to select an item
#print(best_key_so_far)
for a_keys in d_keys:
    if d[a_keys] > d[best_key_so_far]:
        best_key_so_far = a_keys

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

#  Create a dictionary called d that keeps track of all the characters in the string placement and notes
#  how many times each character was seen. Then, find the key with the lowest value in this dictionary
#  and assign that key to min_value.

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

#---------------------------------------------------------------------------------------------------------------
# Assessment for Dictionary Accumulation Lesson
#---------------------------------------------------------------------------------------------------------------

# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is
# the number of credits. Find the total number of credits taken this semester and assign it to the variable credits.
# Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for unitCredit in Junior:
    x = Junior[unitCredit]
    credits = credits + x
print(credits)

# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
str1 = list(str1)
for x in str1:
    if x not in freq:
        freq[x] = 0
    freq[x] += 1
print(freq)

# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts = {}
s1 = list(s1)
for x in s1:
    if x not in counts:
        counts[x] = 0
    counts[x] += 1
print(counts)

# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str1 = str1.split()
freq_words = {}
for each_word in str1:
    if each_word not in freq_words:
        freq_words[each_word] = 0
    freq_words[each_word] += 1
print(freq_words)

# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
sent = sent.split()
wrd_d = {}
for each_word in sent:
    if each_word not in wrd_d:
        wrd_d[each_word] = 0
    wrd_d[each_word] += 1
print(wrd_d)

# Create the dictionary characters that shows each character from the string sally and its frequency.
# Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"

characters = {}
sally = list(sally)
for e_w in sally:
    if e_w not in characters:
        characters[e_w] = 0
    characters[e_w] += 1

freq_keys = characters.keys()
best_char = list(freq_keys)[0]
for each_key in freq_keys:
    if characters[each_key] > characters[best_char]:
        best_char = each_key
print(best_char)
print('cool')

# Find the least frequent letter. Create the dictionary characters that shows each character from string sally
# and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
sally = list(sally)
for e_w in sally:
    if e_w not in characters:
        characters[e_w] = 0
    characters[e_w] += 1

freq_keys = characters.keys()
worst_char = list(freq_keys)[0]
for each_key in freq_keys:
    if characters[each_key] < characters[worst_char]:
        worst_char = each_key
print(worst_char)

# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1.
# Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

string1.lower()
letter_counts = {}

for each_l in string1.lower():
    if each_l not in letter_counts:
        letter_counts[each_l] = 0
    letter_counts[each_l] += 1
print(letter_counts)

# Create a dictionary called low_d that keeps track of all the characters in the string p and notes
# how many times each character was seen. Make sure that there are no repeats of characters as keys,
# such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

p.lower()
low_d = {}

for each_char in p.lower():
    if each_char not in low_d:
        low_d[each_char] = 0
    low_d[each_char] += 1
print(low_d)