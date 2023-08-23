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