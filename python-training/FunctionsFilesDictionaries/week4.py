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