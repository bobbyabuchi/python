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