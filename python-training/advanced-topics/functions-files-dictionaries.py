# Functioms Files and Dictionaries (Week 1) ---------------------------------------------------------------

"""
Files and CSV Output
You will learn how to read from a file, write to a file, and how to work with the .csv data format.
"""

# 10.1. Introduction: Working with Data Files

f = open("I:/tony_montana.txt", "r")
# contents = f.read()
# print(contents)
# l = f.readline()      # read one line
# ls = f.readlines()    # read all the lines and return as a list
lines_list = f.readlines()
line_number = 0
for each_line in lines_list:
    line_number += 1
    print(line_number, each_line)
f.close()

# delete fine
import os
# os.remove("I:/torch.png")

# check if file exist before delete
if os.path.exists("I:/torch.png"):
    os.remove("I:/torch.png")
else:
    print("This file does not exist")

# delete folder (you can only remove empty folders.)
import os
os.rmdir("folder_name")

f = open("I:/movieqs.txt", "r")
contents = f.read()
print(contents[:60]) # read first 60 characters
f.close()

# 10.3. Alternative File Reading Methods

# Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
fayil = open("I:/pydata/school_prompt2.txt")
num_char = len(fayil.read())
print (num_char)

# Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
openFile = open("I:/pydata/travel_plans2.txt")
num_lines = openFile.readlines() # readlines will return a list of all the lines
num_lines = len(num_lines) # len() will tell me the number of items in the list
print(num_lines)

# Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
openFile = open("I:/pydata/emotion_words.txt")
first_forty = openFile.read()
first_forty = (first_forty[:40]) # select the 1st 40 char of the string
print(first_forty)

# 10.4. Iterating over lines in a file

"""
To process all of our olypmics data, we will use a for loop to iterate over the lines of the file. 
Using the split method, we can break each line into a list containing all the fields of interest about the athlete. 
We can then take the values corresponding to name, team and event to construct a simple sentence.
"""
olympicsfile = open("I:/pydata/olympics.txt", "r")

for aline in olympicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

oly = open("I:/pydata/olympics.txt", "r")
ls = oly.readlines()
for each_line in ls:
    values = each_line.split(",")
    print("---------------------------------------------------------------------------------")
    print(values[0],"|",values[1],"|",values[2],"|",values[3],"|",values[4])
    #print("---------------------------------------------------------------------------------")
#print(ls[0],ls[4])

oly = open("I:/pydata/csvPhonebook.txt", "r")
ls = oly.readlines()
for each_line in ls:
    values = each_line.split(",")
    print("--------------------------------------------------------------")
    print(values[0],"|",values[1],"|",values[2],"|",values[3])
    #print("-------------------------------------------------------------")
#print(ls[0],ls[4])

"""
To make the code a little simpler, and to allow for more efficient processing, Python provides a built-in way to iterate through the contents
of a file one line at a time, without first reading them all into a list. Some students find this confusing initially, so we don’t recommend
doing it this way, until you get a little more comfortable with Python. But this idiom is preferred by Python programmers, so you should be
prepared to read it. And when you start dealing with big files, you may notice the efficiency gains of using it.
"""
olympicsfile = open("I:/pydata/olympics.txt", "r")

for aline in olympicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

# 0.6. Using with for Files

md = open('mydata.txt', 'r')
for line in md:
    print(line)
md.close()

# can be written as

# so it closes the file automatically.
with open('I:/pydata/csvPhonebook.txt', 'r') as nnaa:
    for line in nnaa:
        print(line)


# 10.7. Recipe for Reading and Processing a File
"""
#1. Open the file using with and open.

#2. Use .readlines() to get a list of the lines of text in the file.

#3. Use a for loop to iterate through the strings in the list, each being one line from the file. 
On each iteration, process that line of text

#4. When you are done extracting data from the file, continue writing your code outside of the indentation. 
Using with will automatically close the file once the program exits the with block.
"""
# Example:
fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4

"""
However, this will not be good to use when you are working with large data. 
Imagine working with a datafile that has 1000 rows of data. It would take a long time to read in all the data 
and then if you had to iterate over it, even more time would be necessary. 
This would be a case where programmers prefer another option for efficiency reasons.
"""
# This option involves iterating over the file itself while still iterating over each line in the file:
fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    for lin in fileref:                   # step 2
        ## some code that reference the variable lin
#some other code not relying on fileref   # step 3

# 10.8. Writing Text Files

filename = "I:/pydata/squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")
outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()

# 10.10. Reading in data from a CSV File

fileconnection = open("I:/pydata/olympics2.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]                           # store first line in variable header
field_names = header.strip().split(',')     # remove the '\n' and split at the commas
print(field_names)
for row in lines[1:]:                       # for each row from the second line downwards, ie excluding the header [0]
    vals = row.strip().split(',')           # store in val removing '\n' and splitting @ commas
    if vals[5] != "NA":                     # if the val at colum [5] is not NA,
        print("{}: {}; {}".format(          # print so and so columns
            vals[0],
            vals[4],
            vals[5]))

# 10.11. Writing data to a CSV File

"""
The typical pattern for writing data to a CSV file will be to write a header row and loop through the items in a list, 
outputting one row for each. Here we a have a list of tuples, each representing one Olympian, 
a subset of the rows and columns from the file we have been reading from.
"""
# [list of ("t","u","p","l","e"), ("t","u","p","l","e"),("t","u","p","l","e")]
listof = [("t","u","p","l","e"), ("t","u","p","l","e"),("t","u","p","l","e")]

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("I:/pydata/reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    # An alternative, also clear way to do it would be with the .join method:
    # row_string = ','.join(olympian[0], olympian[1], olympian[2]).
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("I:/pydata/reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

# 10.14. Exercises

# Given: sample file called studentdata.txt
"""
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89
"""
# write a program that prints out the names of students that have more than six quiz scores.
f = open("studentdata.txt", "r")
for aline in f:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[0])
f.close()

# Create a list called destination using the data stored in travel_plans.txt.
# Each element of the list should contain a line from the file that lists a country and cities inside that country.
# Hint: each line that has this information also has a colon : in it.


# Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.

# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.
tplans = open("I:/pydata/travel_plans.txt", "r")
content = tplans.read()
# print(content)
num = len(content)
print(num)

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.
num_words = 0
getFile = "I:/pydata/emotion_words.txt"
with open(getFile, 'r') as content:
    for eachline in content:
        num_words += len(eachline.split())
print("number of words : ", num_words)

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
getFile = open("I:/pydata/school_prompt.txt")
content = getFile.readlines()
num_lines = len(content)
print(num_lines)
# Alternatively...
num_lines = sum(1 for eachline in open('I:/pydata/school_prompt.txt'))
print(num_lines)

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
getFile = open("I:/pydata/school_prompt.txt")
content = getFile.read()
beginning_chars = content[:30]
# Alternatively...
getFile = open('I:/pydata/school_prompt.txt', 'r')
beginning_chars = getFile.read(30)
print(beginning_chars)

# Using the file school_prompt.txt, assign the third word of every line to a list called three.
three = []
with open('I:/pydata/school_prompt.txt', 'r') as f:
    three = [line.split()[2] for line in f]
    print(three)

# Create a list called emotions that contains the first word of every line in emotion_words.txt
getFile = open("emotion_words.txt","r")
content = getFile.readlines()
emotions = []
for each_word in content:
    first_word = each_word.split()
    emotions.append(first_word[0])
print(emotions)

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars
getFile = open("I:/pydata/travel_plans.txt")
content = getFile.read()
first_chars = content[:33]
print(first_chars)
# Alternatively...
f = open('I:/pydata/travel_plans.txt', 'r')
first_chars = f.read(33)
print(first_chars)

# Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
getFile = open("school_prompt.txt","r")
p_words=[]
content = getFile.read()
content = content.split()
for each_word in content:
    if 'p' in each_word:
        p_words.append(each_word)
# Alternatively...
fileref = open('school_prompt.txt', 'r')
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]

# Functioms Files and Dictionaries (Week 2) ---------------------------------------------------------------

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

# Functioms Files and Dictionaries (Week 3) ---------------------------------------------------------------

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

# Functioms Files and Dictionaries (Week 4) ---------------------------------------------------------------

"""
More Iteration and Advanced Functions
more advanced iteration mechanism, the while loop. You will be introduced to using it when getting feedback from users,
as well as applying it to the turtle module to draw images. Additionally, you will also be exposed to more advanced function concepts
such as the idea of parameters being optional, not required, and anonymous functions using lambda.
"""

def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """
    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))
print(sumTo(6))
print(sumTo(1000))

# Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number,
# append the counter to a list called eve_nums.
n = -2
eve_nums = []
while n < 14:
    n = n + 2
    eve_nums.append(n)
print(eve_nums)

# just running some checks...
list1 = [8, 3, 4, 5, 6, 7, 9]
print(len(list1))
print(list1[0])

# Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task,
# but instead uses a while loop. Assign the accumulator variable to the name accum.
num = 0
list1 = [8, 3, 4, 5, 6, 7, 9]
accum = 0
tot = 0
for elem in list1:
    tot = tot + elem
print(tot)

# my while loop...
while (num < len(list1)):
    accum = accum + list1[num]
    num += 1
print(accum)

# Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append
# each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(list_num):
    n = 0
    #x = 0
    new_list = []
    while (n < len(list_num)) and (list_num[n] != 4):
        new_list.append(list_num[n])
        n += 1
        #x += 1
    return new_list
print(stop_at_four([1,2,3,4,5,6]))

# 14.3. The Listener Loop

# The loop repeats indefinitely, until a particular input is received.
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)


# Indefinite loops are much more common in the real world than definite loops.
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)
checkout()

# 14.3.1.2. Validating Input
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')


# 14.4. Randomly Walking Turtles
import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()

# 14.5. Break and Continue
# Python provides ways for us to control the flow of iteration with a two keywords: break and continue.

# We can see below how the print statement right after break is not executed. In fact, without using break,
# we have no way to stop the while loop because the condition is always set to True!
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")


# continue is the other keyword that can control the flow of iteration. Using continue allows the program to
# immediately “continue” with the next iteration. The program will skip the rest of the iteration, recheck
# the condition, and maybe does another iteration depending on the condition set for the while loop.
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))


# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while
# loop to return a sublist of the input list. The sublist should contain the same values of the original
# list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(lstr):
    n = 0
    new_list = []
    while 'STOP' not in lstr[n]:
        new_list.append(lstr[n])
        n += 1
    return new_list
print(sublist(['cat','mat','STOP','hat','pat']))

# Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string
# to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(lstr):
    n = 0
    new_list = []
    while 'z' != lstr[n]:
        new_list.append(lstr[n])
        n += 1
    return new_list
print(stop_at_z(['m','a','z','i','Bob']))

# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing,
# but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the
# variable sum2. Once complete, sum2 should equal sum1.
sum2 = 0
sum1 = 0
num = 0
lst = [65, 78, 21, 33]
#...using for loop
for x in lst:
    sum1 = sum1 + x
print(sum1)
#...using while loop
while (num < len(lst)):
    sum2 = sum2 + lst[num]
    num += 1
print(sum2)

# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops
# once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10
# strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned.
# If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge,
# do this without slicing
def beginning(lstr):
    n = 0
    new_list = []
    while 'bye' != lstr[n]:
        new_list.append(lstr[n])
        n += 1
    if len(new_list) > 10:
        return new_list[0:10]
    return new_list
print(beginning(['m','a','z','i','Bob','bye']))

# without slicing
def beginning(lstr):
    n = 0
    new_list = []
    while 'bye' not in lstr[n] and n <10:
        new_list.append(lstr[n])
        n += 1
    if len(new_list) > 10:
        return new_list[0:10]
    return new_list
print(beginning(['m','a','z','i','Bob','bye']))

# 15.1. Introduction: Optional Parameters: specifying default value for parameters with assignment statement
initial = 7
def f(x, y = 3, z = initial):
    print("x,y,z, are: " + str(x) + ", " + str(z))
f(2)
f(2,5)
f(2,5,8)

# The second tricky thing is that if the default value is set to a mutable object, such as a list or a dictionary,
# that object will be shared in all invocations of the function. This can get very confusing, so I suggest that you
# never set a default value that is a mutable object. For example, follow the exceution of this one carefully.
def f(a, L = []):
    L.append(a)
    return L
# When the default value is used, the same list is shared. But on lines 8 and 9 two different copies of the list [“Hello”]
# are provided, so the 4 that is appended is not present in the list that is printed on line 9.
print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Hello"]))
print(f(1))
print(f(5, ["Hello"]))
print(f(4, ["Hello"]))
print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(4, ["Hello"]))

# advfuncs-1-2: What will the following code print?
def f(x = 0, y = 1):
    return x * y
print(f(1)) #  Since one parameter value is specified, it is bound to x; y gets the default value of 1.

# 3. Write a function called str_mult that takes in a required string parameter and an optional integer parameter.
# The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.
def str_mult(x = input('enter string'), y = 3):
    return x * y
print(str_mult())

# 4.7.2. Keyword Arguments
# Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
# accepts one required argument (voltage) and three optional arguments (state, action, and type).
# This function can be called in any of the following ways:
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 15.2.1. Keyword Parameters with .format
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))

# Sometimes, you may want to use the .format method to insert the same value into a string multiple times.
# You can do this by simply passing the same string into the format method, assuming you have included {} s in the string
# everywhere you want to interpolate them. But you can also use positional passing references to do this!
# The order in which you pass arguments into the format method matters: the first one is argument 0,
# the second is argument 1, and so on.
#
# For example,
# this works
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello"))

# advfuncs-2-3: What value will be printed for x?
initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)
f(2, x=5) #  Runtime error since two different values are provided for x
# 2 is bound to x since it's the first value, but so is 5, based on keyword.

# advfuncs-2-4: What value will be printed for z?
# tip: the default value for z is determined at the time the function is defined, not when it is invoked
initial = 7
def f(x, y = 3, z = initial):
    print ("x, y, z are:", x, y, z)
initial = 0
f(2)

# advfuncs-2-5: What value will be printed below?
names = ["Alexey", "Catalina", "Misuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))

# Define a function called multiply. It should have one required parameter, a string. It should also have one optional
# parameter, an integer, named mult_int, with a default value of 10. The function should return the string multiplied by
# the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”)
def multiply(a, mult_int = 10):
    return a * mult_int

# 6. Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code
# doesn’t work. Fix the code so that it passes the test. This should only require changing one line of code.
def waste(var = "Water", mar, marble = "type"): # non default parameter follows default parameter
    final_string = var + " " + marble + " " + mar
    return final_string

# Corrected code
def waste(mar, var = "Water", marble = "type"): # the required parameter 'mar' should come first
    final_string = var + " " + marble + " " + mar
    return final_string

# Lambda notation/expression
def last_char(s):
    return s[-1]
# is the same as:
last_char = (lambda s: s[-1])
# In the typical function, we have to use the keyword return to send back the value. In a lambda function,
# that is not necessary - whatever is placed after the colon is what will be returned.

# If the input to this lambda function is a number, what is returned?
(lambda x: -x)
# A number of the opposite sign (positive number becomes negative, negative becomes positive).

# 15.5. Method Invocations
# To invoke a method, the syntax is <expr>.<methodname>(<additional parameter values>).

# Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True,
# and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True,
# the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned.
# If the boolean parameter is False, return the boolean value “False”.
def test(a, b = True, dict1 = {2:3, 4:5, 6:8}):
    if b == True:
        keyz = list(dict1.keys())
        if a in keyz:
            print (a)
            return dict1[a]
    return False
print(test(6))

# accessing a values with respective keys
dict1 = {2:'Software', 4:'ML', 6:'AI'}
print(dict1[2],dict1[4],dict1[6])

# Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a
# string. The second is an optional parameter called direction with a default value of True. The third is an optional
# parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3,
# 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks
# to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
#
# But if the second paramter is False, then the function should check to see if the first parameter is not a key of
# the third. If it’s not, the function should return True in this case, and if it is, it should return False.
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        keyz = list(d.keys())
        if a in keyz:
            print (a)
            return True
        else:
            return False
    elif direction == False:
        keyz = list(d.keys())
        if a not in keyz:
            print (a)
            return True
        else:
            return False
    return False
print(checkingIfIn(6))

# We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary,
# input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions
# in the active code window for specific variable assignmemts.
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('akara')

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('SE', False, {'ML': 1, 'AI': 9})

# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans= checkingIfIn('fruit')

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('j', True, {'k': 4, 'j': 8, 'v': 16,})

print('c_false: =', c_false)            # False
print('c_true: =', c_true)              # True
print('fruit_ans: =', fruit_ans)        # 19
print('param_check: =', param_check)    # 8

# Functioms Files and Dictionaries (Week 5) ---------------------------------------------------------------

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

# September 2023

"""
Introduction to Functions ----------------------------------------------------------------------------------------------------------------------
"""

"""
Defining and Calling a Void Function ----------------------------------------------------------------------------------------------------------------------
"""

"""
Designing a Program to Use Functions ----------------------------------------------------------------------------------------------------------------------
"""

"""
Local Variables ----------------------------------------------------------------------------------------------------------------------
"""

"""
Passing Arguments to Functions ----------------------------------------------------------------------------------------------------------------------
"""

"""
Global Variables and Global Constants ----------------------------------------------------------------------------------------------------------------------
"""

"""
Introduction to Value-Returning Functions: Generating Random Numbers -----------------------------------------------------------------------------------------
"""

"""
Writing Your Own Value-Returning Functions ----------------------------------------------------------------------------------------------------------------------
"""

"""
The math Module ----------------------------------------------------------------------------------------------------------------------
"""

"""
Storing Functions in Modules ----------------------------------------------------------------------------------------------------------------------
"""

"""
Turtle Graphics: Modularizing Code with Functions -----------------------------------------------------------------------------------------------------------
"""