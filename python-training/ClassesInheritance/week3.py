# course_4_assessment_3

def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM

'''
The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or 
more errors in it. Use this space to write test cases to determine what errors there are. You will be using this 
information to answer the next set of multiple choice questions.
'''

# test-4-1: Which of the following cases fail for the mySum function?
# -> A. an empty list
# -> C. a list with more than one item
'''
Correct, 0 is not returned if the function is given an empty list.
Correct, a list with more than one item does not provide the correct response.
'''

# test-4-2: Are there any other cases, that we can determine based on the current structure of the function, that also
# fail for the mySum function?
# -> B. No
'''
Correct. At the moment we can't tell if other cases would fail (such as combining integers and floats), but it is 
possible that the function could have more issues once the current issues are fixed.
'''

#---------------------------------------------------------------------------------------------------

'''
The class Student is supposed to accept two arguments in its constructor:
A name string

An optional integer representing the number of years the student has been at Michigan (default:1)

Every student has three instance variables:
self.name (set to the name provided)

self.years_UM (set to the number of years the student has been at Michigan)

self.knowledge (initialized to 0)

There are three methods:
.study() should increase self.knowledge by 1 and return None

.getKnowledge() should return the value of self.knowledge

.year_at_umich() should return the value of self.years_UM

There are one or more errors in the class. Use this space to write test cases to determine what errors there are. 
You will be using this information to answer the next set of multiple choice questions.
'''

# test-4-3: Which of the following cases fail for the Student class?
# -> C. the attributes/instance variables are not correctly assigned in the constructor
# -> D. the method study does not increase self.knowledge
'''
Correct! The constructor does not actually use the optional integer that is provided. Instead it sticks with using the default value.
Correct! Study does not increase the self.knowledge.
'''

# test-4-4: Are there any other cases, that we can determine based on the current structure of the class, that also
# fail for the Student class?
# -> A. Yes
'''
Correct! There is an issue with the getKnowledge method because it returns None when self.knowledge is 0, even though 
it returns the correct value when self.knowledge is non-zero.
'''

# 19.2.1. Raising and Catching Errors
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("got an error")

print("continuing")

# If we catch only IndexEror, and we actually have a divide by zero error, the program does stop executing.
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except IndexError:
    print("error 1")

print("continuing")

try:
    x = 5
    y = x/0
    print("This won't print, either")
except IndexError:
    print("error 2")


print("continuing again")

# There’s one other useful feature. The exception code can access a variable that contains information about exactly
# what the error was...print out the information that would normally be printed as an error message
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception, e:
    print("got an error")
    print(e)

print("continuing")

# exceptions-3: After a run-time exception is handled by an except clause, the rest of the code in the try clause
# will be executed?
# -> The rest of the code after the whole try/except statement will execute, but not the rest of the code in the try block

#exceptions-4: How many lines will print out when the following code is executed?
try:
    for i in range(5):
        print(1.0 / (3-i))
except Exception, error_inst:
    print("Got an error", error_inst)

'''
Below, we have provided a list of tuples that consist of student names, final exam scores, and whether or not they will 
pass the class. For some students, the tuple does not have a third element because it is unknown whether or not they 
will pass. Currently, the for loop does not work. Add a try/except clause so the code runs without an error - if there 
is no third element in the tuple, no changes should be made to the dictionary.
'''

students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}

for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except IndexError:
        print('some passing details missing')

print(passing)

'''
Below, we have provided code that does not run. Add a try/except clause so the code runs without errors. If an element 
is not able to undergo the addition operation, the string ‘Error’ should be appended to plus_four.
'''

nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3,
        2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        if num == int(num):
            plus_four.append(num + 4)
        else:
            plus_four.append('Error')
    except TypeError:
        print('Num is not an Integer')

print(plus_four)

# ----------------------------- course_4_assessment_4 ------------------------------------------------

# Q1
'''
The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some 
countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause 
in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the 
string “Did not get gold”.
'''
gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(gold[x])
    except Exception:
        country_gold.append("Did not get gold")

print(country_gold)

# Q2
'''
Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so 
that the code passes.
'''

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
      {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
      {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except KeyError:
        diction['Puppies'] = 0

print("Total number of puppies:", total)

# Q3
'''
The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by 
each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, 
have the string “Error” appear in the remainder.
'''
numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []

for x in numb:
    try:
        n = 36%x
        remainder.append(n)
    except Exception:
        remainder.append("Error")
print(remainder)


# Q4
'''
Provided is buggy code, insert a try/except so that the code passes.
'''
lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except Exception:
        print('Something not right')
print(lst_three)


# Q5
'''
Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, 
have it append to the list attempt the string “Error”.
'''
full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except Exception:
        attempt.append('Error')
print(attempt)


# Q6
'''
The following code tries to append the third element of each list in conts to the new list third_countries. 
Currently, the code does not work. Add a try/except clause so the code runs without errors, and the string 
‘Continent does not have 3 countries’ is appended to countries instead of producing an error.
'''
conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'],
         ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'],
         ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'],
         ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except Exception:
        third_countries.append('Continent does not have 3 countries')

print(third_countries)

# Q7
'''
The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code will run 
properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.
'''
sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except Exception:
        print(x, 'not in dictionary, added', x)
        ppl_play[x] = 1

print(ppl_play)

# Q8
'''
Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so 
that the code passes. If the key is not there, initialize it in the dictionary and set the value to zero.
'''
di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except Exception:
        diction['Puppies'] = 0
print("Total number of puppies:", total)
