# from the book: Starting out with Python by Tony Graddis

#Basic Python Elements
"""
1.Input, Processing Output
2.Simple Functions
3.Decision Structure and Boolean Logic
4.Repetition Structures
5.Value-Returning Functions and Modules
6.Files and Exceptions
7.Lists and Tuples
8.More About Strings
9.Dictionaries & Sets
10.Classes & Object-Oriented Programming
11.Inheritance
12.Recursion
"""

#(1.1) Designing a Program
#-----------------------------------------------------------------------------

'''
The process of designing a program can be summarized in the following two steps:
1. Understand the task that the program is to perform.
2. Determine the steps that must be taken to perform the task.
'''
# (1.2) INPUT, PROCESSING AND OUTPUT
#-----------------------------------------------------------------------------
'''
Computer programs typically perform the following three-step process:
1. Input is received.
2. Some process is performed on the input.
3. Output is produced.
'''

print('Hello world')

numberX = int(input('enter any number: '))
outPut = (numberX + 100)
print(outPut)

# Simple Age Calculator
birthYear = input("Enter your of birth ")
currentYear = 2019
age = (currentYear - birthYear)
print (age)

x = 22
y = 2
z = (x+y)
print(z)



print(username)

#--Calculate Annual Salary of a User
#----------------------------------------------------------------------------

# Get the user's name, currency, and income.
name = input('What is your name? ')
currency = (input('What currency are you paid in? '))
income = float(input('What is your monthly income? '))
ansa = (12 * income)

# Display the data.
message = "Thank you {}, your annual salary is {} {}"
print(message.format(name, ansa, currency))

#Inserting Comma Separators: insert a comma into the format specifier
print(format(ansa, ',.2f'))
print(message.format(name, format(ansa, ',.2f'), currency))



#Get three test scores and assign them to the
#----------------------------------------------------------------------------
# test1, test2, and test3 variables.
ca1 = float(input('Enter the first test score: '))
ca2 = float(input('Enter the second test score: '))
exam = float(input('Enter the third test score: '))

# Calculate the average of the three scores
# and assign the result to the average variable.
average = (ca1 + ca2 + exam) / 3

# Display the average.
print('The average score is', average)

#format() result to 2 decimal places
print('The average score is', format(average, '.2f'))


#(1.3) Displaying Output with the print Function
#-----------------------------------------------------------------------------

print('Hello world')

#...printing strings with apostrophe
print("Don't fear")
print('I\'m here.')

print('Your assigment is to be read "Hamlet" by tomorrow')# print a quote within a string
print("""T'm reading "Chronicles of Narnia" tonight.""")# print string with qoute and apostrophe
print(""" line1:and of course this is
line2: how you pring multiline
line3: strings""")

import random # will explain modules later...
print(random.randrange(1,10))

#(1.4) Comments
#-----------------------------------------------------------------------------
#...single line
"""
multi
line
comment
"""

#(1.5) Variables (a name that represents a value stored in the computer's memory)
#-----------------------------------------------------------------------------

age = 12
answer = 2
text = 'a string value'

# Create two variables: top_speed and distance.
top_speed = 160
distance = 300

# Display the values referenced by the variables.
print('The top speed is')
print(top_speed)
print('The distance traveled is')
print(distance)

#...variable reassignment
dollars = 10.99
print('I have', dollars, 'in my account.')

# Reassign dollars so it references
# a different value.
dollars = 2000.95
print('But now I have', dollars, 'in my account!')

#(1.6) Reading Input from the Keyboard
#-----------------------------------------------------------------------------

# Get the user's first name.
first_name = input('Enter your first name: ')

# Get the user's last name.
last_name = input('Enter your last name: ')

# Print a greeting to the user.
print('Hello', first_name, last_name)

#(1.7) Performing Calculations
#-----------------------------------------------------------------------------

# Assign a value to the salary variable.
salary = 2500.0

# Assign a value to the bonus variable.
bonus = 1200.0

# Calculate the total pay by adding salary
# and bonus. Assign the result to pay.
pay = salary + bonus

# Display the pay.
print('Your pay is', pay)

#..This program gets an item's original price and
# calculates its sale price, with a 20% discount.

#Get the item's original price.
original_price = float(input("Enter the item's original price: "))

 # Calculate the amount of the discount.
discount = original_price * 0.2

 # Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print('The sale price is', sale_price)

#...(test_score_average.py)

# Get three test scores and assign them to the
# test1, test2, and test3 variables.
test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))
# Calculate the average of the three scores
# and assign the result to the average variable.
average = (test1 + test2 + test3) / 3.0
# Display the average.
print('The average score is', average)

#...(time_converter.py)

# Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds: '))
# Get the number of hours.
hours = total_seconds // 3600
# Get the number of remaining minutes.
minutes = (total_seconds // 60) % 60
# Get the number of remaining seconds.
seconds = total_seconds % 60
# Display the results.
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes);
print('Seconds:', seconds)


#...breaking long statements into multi-line
units_sold = 24
sales_amount = 50
print('We sold,', units_sold, 'for a total of,', sales_amount)
#...multi-line
print('We sold',\
      units_sold, \
      'for a total of', \
      sales_amount)

#...my observation on concatenation
#this will give us error...why?
print('We sold,' units_sold 'for a total of,' sales_amount)
#this is okay...so we can just concatenate with comma.
print('We sold,', units_sold, 'for a total of,', sales_amount)

#(1.8) More About Data Output
#-----------------------------------------------------------------------------

print('One')
print('Two')
print('Three')
#...if you do not want the print() to automatically insert a new line
print('One', end=' ')
print('Two', end=' ')
print('Three')

#...print without a space inbetween
print('One', end='')
print('Two', end='')
print('Three')

#...Specifying an Item Separator
print('One', 'Two', 'Three', sep='')

#...escape characters (\) 
print('One\nTwo\nThree') #(\n) is is used to insert a new line in the print statement
print('I want to do God\'s will.') # (\) is used here to ignore the single qoute insde single qoute
"""
some of Python's Escape Character
(\n) - insert next line
(\t) - skip to next hori
(\') - print single qoute in a single qoute
(\") - print double in double
(\\) - print backslash(\)
"""
#Displaying Multiple items with the + Operator
print('This is one string' + ' and yet another string.') # the + will append other strings to the first one
#...formatting numbers with the format() specifier

print('Enter the amount of ' + \
'sales for each day and ' + \
'press Enter.')

#...Formatting Numbers
#...rounding to desired decimal place
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print('The monthly payment is', monthly_payment)
print('formatted monthly payment is', format(monthly_payment, '.2f'))#.2f means 2 decimal places

#...Formatting in Scientific Notation
print(format(12345.6789, 'e'))
print(format(12345.6789, '.2e'))

#...Formatting with Comma Separators
print(format(12345.6789, ',.2f'))
print(format(123456789.456, ',.2f'))
print(format(12345.6789, ',f'))

#..displaying floating-point number as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is N', \
      format(annual_pay, ',.2f'), \
      sep='') #...the sep='' argument is to eliminate space bwn N and amt

#...Specifying a Minimum Field Width
print('The number is', format(12345.6789, '12,.2f'))#minimum of 12 spaces
print('The number is', format(12345.6789, '12.2f'))#spaceout without comma sep

#...display floating pts in a column with alignment
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
#formant and align
print(format(num1, '10.2f'))
print(format(num2, '10.2f'))
print(format(num3, '10.2f'))
print(format(num4, '10.2f'))
print(format(num5, '10.2f'))
print(format(num6, '10.2f'))


#...Formatting a Floating-Point Number as a Percentage
print(format(0.5, '%'))#...% will multiply the number by 100 and put % in front
print(format(0.5, '.2%'))
print(format(0.5, '.0%'))

#...Formatting Integers int() data types...no need for precision/decimal place here so...
#...writing a format specifier for an int, keep in mind that
#...• You use d as the type designator.
#...• You cannot specify precision.

print(format(123456, 'd')) # no special formatting
print(format(123456, ',d')) # with a comma sep

print(format(123456, '10d')) # with 10 spaces wide
print(format(123456, '10,d')) # 10 spaces wide and comma sep

#STRINGS: 
"""
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
"""
#---------------------------------------------------------------------------
"""
String Literals
String literals in python are surrounded by
either single quotation marks,
or double quotation marks.
'hello' is the same as "hello".
"""

#You can display a string literal with the print() function:
print("Hello")
print('Hello')

#--escape\backslash when using single qoute
print('Hello my name is God\'s will.')
print("Hello my name is God's will.")

#--Assign String to a Variable
a = "Hello"
print(a) 

#--Multiline Strings: by using three quotes (double/single):
pledge = """I pledge to Nigeria my Country;
To be faithful, loyal and honest;
To serve Nigeria with all my strength;
To defend her unity;
And uphold her honour and glory;
So help me God."""
print(pledge)

#--Strings as Arrays
"""
strings in Python are arrays of
(bytes representing unicode) characters.
"""
#Get the character at position 1
#(remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#--Substring. Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#--The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

#--The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))

#--The lower() method returns the string in lower case: 
a = "Hello, World!"
print(a.lower())

#--The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#--The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#--The split() method splits the string into substrings
#--if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
#--'str'.split(sep=None, maxsplit=-1)
'1,,2'.split(',')
'1<>2<>3'.split('<>')
'a, b, c, d'.split(',')

#String Format: we cannot combine strings and
#--numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)
"""
But we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them,
and places them in the string where the placeholders {} are:
"""
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments,
#--and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#--You can use index numbers {0} to be sure the arguments are placed
#--in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#--use len() method to print the length of a str
len('abcde')
print(len('abcde'))



# SIMPLE FUNCTIONS
#-----------------------------------------------------------------------------
"""
def function_name():
      statement
      statement
      .
      .
      .
      etc.

- A function is a group of statements that exist within a
      program for the purpose of performing a specific task....
- Instead of writing a large program as one long sequence of statements, 
      it can be written as several small functions, each one performing 
      a specific part of the task. executed in the desired order to 
      perform the overall task.This approach is aka 'divide and conquer'
- functions enable you to write a code once and then reuse it each time
      you need to perform that task
- functions facilitates team work, easily divide task among programmers
 """
 #...naming functions, chose meaningful names wrt what it does...like in naming variables

#(2.2) Defining and Calling a Function
#-----------------------------------------------------------------------------

#...function_demo.py
def message():
      print('I am Arthur,')
      print('King of the Brits.')
message()

#...two_functions.py
def main(): #define the main()
      print('I have a message for you.')
      message()
      print('Goodbye')

def message(): #define the message()
      print('I am Arthur, ')
      print('King of the Brits.')

main() # call the main()

#(2.3) Designing a Program to Use Functions
#-----------------------------------------------------------------------------

#...in a flowchart, a function call is shown with a rectangle that has vertical bars
"""
-----------------------
| |                 | |
| | function_name() | |
| |                 | |
-----------------------
"""
#...*hierarchy charts: depict visual representation of the relationships between functions.*

#...ace_dryerApp.py
# This program displays step-by-step instructions
#...for disassembling an Ace dryer.
#...The main function performs the program's main logic.

def main(): # Display the start-up message.
      startup_message()
      input('Press Enter to see Step 1.')
      step1() # Display step 1.
      input('Press Enter to see Step 2.')
      step2() # Display step 2.
      input('Press Enter to see Step 3.')
      step3() # Display step 3.
      input('Press Enter to see Step 4.')
      step4() # Display step 4.

# The startup_message function displays the
# program's initial message on the screen.
def startup_message():
      print('This program tells you how to')
      print('disassemble an ACME laundry dryer.')
      print('There are 4 steps in the process.')
      print()

# The step1 function displays the instructions
# for step 1.
def step1():
      print('Step 1: Unplug the dryer and')
      print('move it away from the wall.')
      print()

# The step2 function displays the instructions
# for step 2.
def step2():
      print('Step 2: Remove the six screws')
      print('from the back of the dryer.')
      print()

# The step3 function displays the instructions
# for step 3.
def step3():
      print('Step 3: Remove the back panel')
      print('from the dryer.')
      print()

# The step4 function displays the instructions
# for step 4.
def step4():
      print('Step 4: Pull the top of the')
      print('dryer straight up.')

# Call the main function to begin the program.
main()

#(2.4) Local Variables
#-----------------------------------------------------------------------------
"""
    a local vaiable is a variable that exists within a function
    and cannot be accessed by statements outside the function.
    -> note also that a local variable cannot be accessed by code/statements
       that exist before their  
"""
#...Scope & Local Variables (bad_local.py)
def main():# Definition of the main function.
      get_name()
      print('Hello', name) # This causes an error! because name is localised in another function outside the main()

def get_name():# Definition of the get_name function.
      name = input('Enter your name: ')

main()# Call the main function.

def bad_function():
      print('The value is', val) # This will cause an error!
      val = 99

bad_function()

#...birds.py
#...two functions can have local variables with the same name
def nigeria():
      abuja()#call texas funct
      lagos() # call lagos

def abuja():
      slogan = 'Center of Unity'
      print ('Abuja is the ',slogan)

def lagos():
      slogan = 'Center of Excellence'
      print ('Lagos is the ',slogan)

nigeria()


#(2.5) Passing Arguments to Functions
#-----------------------------------------------------------------------------
"""
An argument is any piece of data
 that is passed into a function when the
 function is called... 
"""
#...pass_arg.py
def main():
      value = 5
      show_double(value)
def show_double(number):
      result = number*2
      print(result)
main()

#(2.6) Global Variables and Global Constants
#-----------------------------------------------------------------------------

#...A global variable is accessible to all the functions in a program file.
myValue = 10 # a global variable

def showValue():
      localVariable = 200 # a local variable
      print(myValue)
      print(localVariable)
showValue()

print(localVaraible) # this will give an error because it is only defined within a function

#...retirement.py
# The following is used as a global constant
# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
      gross_pay = float(input('Enter the gross pay: '))
      bonus = float(input('Enter the amount of bonuses: '))
      show_pay_contrib(gross_pay)
      show_bonus_contrib(bonus)

# The show_pay_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.
def show_pay_contrib(gross):
      contrib = gross * CONTRIBUTION_RATE
      print('Contribution for gross pay: $', \
      format(contrib, ',.2f'), \
      sep='')

# The show_bonus_contrib function accepts the
# bonus amount as an argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
      contrib = bonus * CONTRIBUTION_RATE
      print('Contribution for gross pay: $', \
      format(contrib, ',.2f'), \
      sep='')

main()# Call the main function.

# DECISION STRUCTURES AND BOOLEAN LOGIC

#(3.1) The if Statement
#-----------------------------------------------------------------------------

#...test_average.py
#...(this program gets 3 scores and displays avg conragtulates high avg)

HIGH_SCORE = 95 # declare hi score as global constant
def main():
      #get 3 test scores
      Ca1 = int(input('Enter First C/A: '))
      Ca2 = int(input('Enter Second C/A: '))
      exam = int(input('Enter ExamScore: '))
      #cal the avg score
      avg = (Ca1 + Ca2 + exam) / 3
      #print the avg
      print('The avg score is', avg)
      #congratulate user if avg score is high
      if avg >= HIGH_SCORE:
            print ('Congratulations! ')
            print('What a great average!')
main()

#(3.2) The if-else Statement
#-----------------------------------------------------------------------------

"""
An if-else statement will execute one block of statements if its condition
is true, or another block if its condition is false.
"""

#(3.3) Comparing Strings
#-----------------------------------------------------------------------------

"""Python allows you to compare strings. This allows you to create decision
structures that test the value of a string."""

#(3.4) Nested Decision Structures and the if-elif-else Statement
#-----------------------------------------------------------------------------

"""To test more than one condition, a decision structure can be nested
inside another decision structure."""

#...grader.py
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

#..if-else nested format
def main():
      score = int(input('Enter your test score: '))
      if score >= A_SCORE:
            print('That\'s an A.')
      else:
            if score >= B_SCORE:
                  print('That\'s a B.')
            else:
                  if score >= C_SCORE:
                        print('That\'s a C.')
                  else:
                        if score >= D_SCORE:
                              print('That\'s a D.')
                        else:
                              print('That\'s an F.')
main()

#..same code above but in if-elif-else format
def main():
      score = int(input('Enter your test score: '))
      if score >= A_SCORE:
            print('Your grade is A.')
      elif score >= B_SCORE:
            print('Your grade is B.')
      elif score >= C_SCORE:
            print('Your grade is C.')
      elif score >= D_SCORE:
            print('Your grade is D.')
      else:
            print('Your grade is F.')
main()

#(3.5) Logical Operators
#-----------------------------------------------------------------------------
"""The logical 'AND' operator and the logical 'OR' operator allow you to connect
multiple Boolean expressions to create a compound expression. The
logical 'NOT' operator reverses the truth of a Boolean expression."""

MIN_SALARY = 30000.0
MIN_YEARS = 2

def main():
      # Get the customer's annual salary.
      salary = float(input('Enter your annual salary: '))
      # Get the number of years on the current job.
      years_on_job = int(input('Enter the number of ' +
      'years employed: '))
      # Determine whether the customer qualifies.
      if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
            print('You qualify for the loan.')
      else:
            print('You do not qualify for this loan!')
# Call the main function.
main()

#(3.6) Boolean Variables
#-----------------------------------------------------------------------------
"""
A Boolean variable reference one of two values: True or False.
They're commonly used as flags, to indicate whether specific conditions exist.
"""
x = True
y = False


#(4.1) REPETITION STRUCTURES aka LOOPS
#-----------------------------------------------------------------------------
"""
#...make a stament or set, execture repeatedly
# - ConditionControlled: a statement or set of statements to repeat as long as a condition is true
# - Count controlled runs a specific no. of times
"""
#...The 'while Loop': a Condition-Controlled Loop (while a condition is true, do this...)
      # This program calculates sales commissions.
def main():
      keep_going = 'y' # Create a variable to control the loop.
            # Calculate a series of commissions.
      while keep_going == 'y':
                  # Get a salesperson's sales and commission rate.
            sales = float(input('Enter the amount of sales: '))
            comm_rate = float(input('Enter the commission rate: '))
                  # Calculate the commission.
            commission = sales * comm_rate
                  # Display the commission.
            print('The commission is $', \
            format(commission, ',.2f'), sep='')
                  # See if the user wants to do another one.
            keep_going = input('Do you want to calculate another ' + \
            'commission (Enter y for yes): ')
main() # Call the main function.

#...the is program prints number 1 to 100 and the stop
def iLoop():            #...define function
      x = 0             #...set a local variable 'x'
      while x <= 99:    #...while this set condition (the value of 'x' is '<' or '=' 100) is true
            x = (x+1)   #...add '1' to 'x'
            print (x)   #...print 'x'
iLoop()                 #...call the function

#...the is program prints number 1 to infinity and never stop...
def infiniteLoop():            #...define function
      x = 0             #...set a local variable 'x'
      while x >= 0:    #...while this set condition (the value of 'x' is '>' or '=' 0) is true
            x = (x+1)   #...add '1' to 'x'
            print (x)   #...print 'x'
infiniteLoop()                 #...call the function

#...this program assist a technician in the process of monitoring a substance's temperature
MAX_TEMP = 102.5 # max temp. set as a global constant
def main():
            #..get the substance's temperature
      temp = float(input('Enter the substance\'s Celsius temperature: '))
      while temp > MAX_TEMP:
            print('Too High!')
            print('Turn the thermostat down and wait')
            print('5 minutes. Then take the temperature')
            print('again and enter it.')
            temp = float(input('Enter the new Celsius temperature: '))
      print('The temperature is acceptable.')
      print('Check it again in 15 minutes.')
main()

#...this program demonstrates and infinite loop
def main():
            #...create variable to control the loop
      x = 'y'
            #...warning! infinite loop!
      while x == 'y':
            sales = float(input('Enter amont of sales: '))
            common_rate = float(input('Enter the commission rate: '))
                  #...calculate the commission
            commission = sales * common_rate
                  #...display commission
            print('The commission is $', \
                  format(commission, ',.2f'), sep='')
      #...call main function
main()

#...Calling Functions in a Loop
#...commission20.py
def main():
            # create a variable to control the loop
      x = 'y'
            # calculate a serries of commissiion
      while x == 'y':
                  # call function to display a salesperson's commission
            showCommission()
                  # see if the user wants to do another one
            print('Do you want to calculate another commission?')
            x = input('Enter \'y\' for yes: ')
# the showCommission() gets the amount of sales and commission rate, and displays the commission
def showCommission():
      sales = float(input('Enter the amount of sales: '))
      common_rate = float(input('Enter the commission rate: '))
            # calculate the commission
      commission = sales * common_rate
            # dislpay the commission
      print('The commission is $', format(commission, ',.2f'), sep='')
main()

#...The for Loop: a Count-Controlled Loop
"""A count-controlled loop iterates a specific number of times.
the 'for' statement to write a count-controlled loop."""

# This program demonstrates a simple for loop
# that uses a list of numbers.
def main():
      print('I will display the numbers 1 through 5.')
      for num in [1, 2, 3, 4, 5]: #targert variable
            print(num)
main()

def main():
      for animals in ['Bird', 'Mbe', 'Nkita', 'Ugolooma', 'Eneke_nti_oba', 'Ozo', 'Mgbada']:
            print (animals)
main()

#...using range function in 'for' loop
def main():
      for num in range(5):
            print (num)
main()

def main():
            # print message 5x
      for x in range(5):
            print('Jindu Jessie ')
main()


# VALUE-RETURNING FUNCTIONS
#-----------------------------------------------------------------------------


# FILES AND EXCEPTIONS
#-----------------------------------------------------------------------------

# LISTS AND TUPLES
#-----------------------------------------------------------------------------

# MORE ABOUT STRINGS
#-----------------------------------------------------------------------------

# DICTIONARIES AND SETS
#-----------------------------------------------------------------------------

# CLASSES AND OBJECT-ORIENTED PROGRAMMING
#-----------------------------------------------------------------------------

# INHERITANCE
#-----------------------------------------------------------------------------

# RECURSION
#-----------------------------------------------------------------------------

# GUI PROGRAMMING
#-----------------------------------------------------------------------------

# 
#-----------------------------------------------------------------------------

#(6.1) title
#-----------------------------------------------------------------------------

#(6.2) title
#-----------------------------------------------------------------------------

#(6.3) title
#-----------------------------------------------------------------------------

#(6.4) title
#-----------------------------------------------------------------------------
#(7.1) title
#-----------------------------------------------------------------------------
#(7.2) title
#-----------------------------------------------------------------------------
#(7.3) title
#-----------------------------------------------------------------------------
#(7.4) title
#-----------------------------------------------------------------------------
#(7.5) title
#-----------------------------------------------------------------------------
#(7.6) title
#-----------------------------------------------------------------------------
#(7.7) title
#-----------------------------------------------------------------------------
#(7.8) title
#-----------------------------------------------------------------------------
#(7.9) title
#-----------------------------------------------------------------------------
#(8.1) title
#-----------------------------------------------------------------------------
#(8.2) title
#-----------------------------------------------------------------------------
#(8.3) title
#-----------------------------------------------------------------------------
#(9.1) title
#-----------------------------------------------------------------------------
#(9.2) title
#-----------------------------------------------------------------------------
#(9.3) title
#-----------------------------------------------------------------------------
#(10.1) title
#-----------------------------------------------------------------------------
#(10.2) title
#-----------------------------------------------------------------------------
#(10.3) title
#-----------------------------------------------------------------------------
#(10.4) title
#-----------------------------------------------------------------------------
#(11.1) Introduction to Inheritance
#-----------------------------------------------------------------------------
#(11.2) Polymorphism
#-----------------------------------------------------------------------------
#(12.1) Introduction to Recursion
#-----------------------------------------------------------------------------
#(12.2) Problem Solving with Recursion
#-----------------------------------------------------------------------------
#(12.3) Examples of Recursive Algorithms
#-----------------------------------------------------------------------------
"""
.
.-- N D
.
"""
# NOTES VARIABLES

""" 
Design the Program All professional programmers will tell you that a program
should be carefully designed before the code is actually written.

The process of designing a program can be summarized in the following two steps:
1. Understand the task that the program is to perform.
2. Determine the steps that must be taken to perform the task.

It is essential that you understand what a program is supposed to do before you can determine
the steps that the program will perform.

Typically, a professional programmer gains this understanding by working directly with the customer.
A customer is a person, group, or organization that is asking you to write a program.
This could be a customer in the traditional sense of the word, meaning someone who is paying you to write a program.
It could also be your boss, or the manager of a department within your company.
Regardless of whom it is, the customer will be relying on your program to perform an important task.

To get a sense of what a program is supposed to do, the programmer usually interviews the
customer. During the interview, the customer will describe the task that the program should
perform, and the programmer will ask questions to uncover as many details as possible about
the task. A follow-up interview is usually needed because customers rarely mention everything
they want during the initial meeting, and programmers often think of additional questions.

The programmer STUDIES the information that was gathered from the customer during the interviews
and creates a list of different software requirements. A software requirement is simply a
single task that the program must perform in order to satisfy the customer. Once the customer
agrees that the list of requirements is complete, the programmer can move to the next phase.

Once you understand the task that the program will perform, you begin by breaking down
the task into a series of steps.

For example, suppose someone asks you
how to boil water. You might break down that task into a series of steps as follows:
1. Pour the desired amount of water into a pot.
2. Put the pot on a stove burner.
3. Turn the burner to high.
4. Watch the water until you see large bubbles rapidly rising. When this happens, the
water is boiling.

This is an example of an algorithm,, which is a set of well-defined logical steps that must be
taken to perform a task. Notice that the steps in this algorithm are sequentially ordered. Step 1
should be performed before step 2, and so on. If a person follows these steps exactly as they
appear, and in the correct order, he or she should be able to boil water successfully.

A programmer breaks down the task that a program must perform in a similar way. An
algorithm is created, which lists all of the logical steps that must be taken. For example,
suppose you have been asked to write a program to calculate and display the gross pay for
an hourly paid employee.

Here are the steps that you would take:
1. Get the number of hours worked.
2. Get the hourly pay rate.
3. Multiply the number of hours worked by the hourly pay rate.
4. Display the result of the calculation that was performed in step 3.

Of course, this algorithm isn’t ready to be executed on the computer. The steps in this list
have to be translated into code. Programmers commonly use two tools to help them accomplish
this: pseudocode and flowcharts.

FLOWCHART
• The ovals, which appear at the top and bottom of the flowchart, are called terminal
symbols. The Start terminal symbol marks the program’s starting point and the End
terminal symbol marks the program’s ending point.
• Parallelograms are used as input symbols and output symbols. They represent steps in
which the program reads input or displays output.
• Rectangles are used as processing symbols. They represent steps in which the program
performs some process on data, such as a mathematical calculation.

Checkpoint
2.1 Who is a programmer’s customer?
2.2 What is a software requirement?
2.3 What is an algorithm?
2.4 What is pseudocode?
"""
#Ref. Starting out with Python by Tony Gaddis