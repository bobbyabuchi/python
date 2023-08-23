class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0


class AnotherPoint:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(chi):
        chi.x = 0
        chi.y = 0


p = AnotherPoint()         # Instantiate an object of type Point
q = AnotherPoint()         # and make a second point
print("Nothing seems to have happened with the points")

print(p)
print(q)
print(p is q)

# Adding Parameters to the Constructor
class yetAnotherPoint:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
p = yetAnotherPoint(7,6)
print(p)

#------------------------------------------------------------------------------------------------
# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
print(MyClass)

# Create an object named p1, and print the value of x:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
print(p1)
#----------------------------------------------------------------------------------------------
# The examples above are classes and objects in their simplest form, not really useful in real life applications.

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.name = 'Chisom'
p1.age = 27
print(p1.name, 'is', p1.age)

# Delete the age property from the p1 object:
del p1.age

# Delete the p1 object:
del p1

# Pass statement: just because you can't leave a class def empty. so just give it a pass
class Mmadu:
  pass



# Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2,
# which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10.
# Save this instance to a variable t.
class NumberSet:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
t = NumberSet(6, 10)
print(t.num1)
print(t.num2)

# 20.5. Adding Other Methods to a Class

# add two simple methods to allow a point to give us information about its state.
class Point1:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


p = Point1(7,6)
print(p.getX())
print(p.getY())

# Let’s add another method, distanceFromOrigin, to see better how methods work. This method will again not need any
# additional information to do its work, beyond the data stored in the instance variables.
# It will perform a more complex task.


class Point2:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, init_x, init_y):

        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point2(7,6)
print(p.distance_from_origin())

# Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance
# variables: arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs
# the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs
# method on the spider instance and save the result to the variable name spidlimbs.

# Create a class called Animal that accepts two numbers as inputs and assigns
# them respectively to two instance variables:Create a class called Animal that
# accepts two numbers as inputs and assigns them respectively to two instance variables:


class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs
# Create an instance method called limbs that, when called, returns the total number
# of limbs the animal has.

    def limbs(self):
        return self.arms + self.legs
# Call the limbs method on the spider instance and save the result to the
# variable name spidlimbs.


spider = Animal(4,4)
spidlimbs = spider.limbs()

# 20.6. Objects as Arguments and Parameters: You can pass an object as an argument to a function, in the usual way.

# Here is a simple function called distance involving our new Point objects.
# The job of this function is to figure out the distance between two points.

import math

class Point1:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # this is to show that
    def distance(self, point2):
        xdiff = point2.get_x() - self.get_x()
        ydiff = point2.get_y() - self.get_y()

        dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
        return dist

# distance is not a method of the Point class.
# You can see this by looking at the indentation pattern.
# and self is not a parameter here
def a_distance(point1, point2):
    xdiff = point2.get_x()-point1.get_x()
    ydiff = point2.get_y()-point1.get_y()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point1(4,6)
q = Point1(2,3)
print(a_distance(p,q))

# because distance is made a method of the Point class, we can call the first parameter self,
# and invoke it using the dot notation, just a matter of coding style. Both work correctly
print(p.distance(q))

"""
Most programmers choose whether to make functions be stand-alone or methods of a class based on whether the function 
semantically seems to be an operation that is performed on instances of the class. In this case, because distance is 
really a property of a pair of points and is symmetric (the distance from a to b is the same as that from b to a) it 
makes more sense to have it be a standalone function and not a method. Many heated (heated? lol) discussions have 
occurred between programmers about such style decisions.
"""

# 20.7. Converting an Object to a String
# When we’re working with classes and objects, it is often necessary to print an object
# (that is, to print the state of an object). Consider the example below.

class Point2:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    # The __str__ method is responsible for returning a string representation as defined by the class creator
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point2(7,6)
print(p)


# Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance
# variables in the constructor: name, brand, and fiber. When an instance of Cereal is printed, the user should see
# the following: “[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!”
# To the variable name c1, assign an instance of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber
# is 2. To the variable name c2, assign an instance of Cereal whose name is "Honey Nut Cheerios", brand is
# "General Mills", and fiber is 3. Practice printing both!

class Cereal:
    def __init__(self, n, b, f):
        self.name = n
        self.brand = b
        self.fiber = f

    def get_n(self):
        return self.name

    def get_b(self):
        return self.brand

    def get_f(self):
        return self.fiber

    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand,
                                                                                                self.fiber)


c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)

# 20.8. Instances as Return Values

# Suppose you have a point object and wish to find the midpoint halfway between it and some other target point.
# We would like to write a method, let’s call it halfway, which takes another Point as a parameter and returns
# the Point that is halfway between the point and the target point it accepts as input.
class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what

print(mid)
print(mid.getX())
print(mid.getY())
# The resulting Point, mid, has an x value of 4 and a y value of 8. We can also use any other methods on mid
# since it is a Point object.


# 20.9. Sorting Lists of Instances
L = ["Cherry", "Apple", "Blueberry"]

# in the example below, we write key=len and not key=len()
print(sorted(L, key=len))
#alternative form using lambda, if you find that easier to understand
print(sorted(L, key= lambda x: len(x)))


# When each of the items in a list is an instance of a class, you need to provide a function that takes one instance
# as an input, and returns a number. The instances will be sorted by their numbers
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)


# defined a method sort_priority that does some computation on the data in an instance
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)


# 20.10. Class Variables and Instance Variables

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())


# Test Cases: Checking Assumptions About Data Types

# In the code below, we explicitly state some natural assumptions about how truncated division might work in python.
# It turns out that the second asumption is wrong: 9.0//5 produces 2.0, a floating point value!
assert type(9//5) == int
assert type(9.0//5) == int

# In the code below, lst is bound to a list object. In python, not all the elements of a list have to be of the same
# type. We can check that they all have the same type and get an error if they are not. Notice that with lst2,
# one of the assertions fails.
lst = ['a', 'b', 'c']

first_type = type(lst[0])
for item in lst:
    assert type(item) == first_type

lst2 = ['a', 'b', 'c', 17]
first_type = type(lst2[0])
for item in lst2:
    assert type(item) == first_type

# We can also check other assumptions about the values of variables, in addition to their types. For example,
# we could check that a list has fewer than 10 items.
lst = ['a', 'b', 'c']
assert len(lst) < 10

# In this case, you’ll never get an error, no matter the values of x and y.
x = 3
y = 4
if x < y:
    z = x
else:
    if x > y:
        z = y
    else:
        ## x must be equal to y
        assert x==y
        z = 0

# Testing Loops
# When lst is [1, 5, 8], the value at the end should be 14.
nums = [1, 5, 8]
accum = 0
for w in nums:
    accum = accum + w
assert accum == 14

#  given an empty list...suppose we wanted it to be some other value, perhaps the special python value None
nums = []

accum = 0
for w in nums:
    accum = accum + w
assert accum == None

# ...and fixing our accumulator code
nums = []

if len(nums) == 0:
   accum = None
else:
   accum = 0
   for w in nums:
       accum = accum + w
assert accum == None

# Writing Test Cases for Functions
def square(x):
    return x*x
assert square(3) == 9

# Side Effect Tests: test whether a function makes correct changes to a mutable object
def update_counts(letters, counts_d):
    for c in letters:
        counts_d[c] = 1
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1

counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3

# Testing Optional Parameters: when no parameter value is supplied during execution
assert sorted([1, 7, 4]) == [1, 4, 7]
assert sorted([1, 7, 4], reverse=True) == [7, 4, 1]

# When testing a function, it is essential to know the right answer.

# The distance between any point and itself should be 0
def distance(x1, y1, x2, y2):
    return None

assert distance(1, 2, 1, 2) == 0

# It’s not returning the correct answer, so we don’t pass the test. Let’s fix that.
def distance(x1, y1, x2, y2):
    return 0.0

assert distance(1, 2, 1, 2) == 0

# the horizontal distance equals 3 and the vertical distance equals 4; that way, the result is 5
def distance(x1, y1, x2, y2):
    return 0

assert distance(1, 2, 1, 2) == 0
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) == 2**0.5


# side effect test
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

assert distance(1, 2, 1, 2) == 0
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) == 2**0.5

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7


# 20.12. Testing classes

# test-3-2: To test a method that changes the value of an instance variable, which kind of test case should you write?
# -> side effect test:

# week 1 assessment
# (No. 1)
# Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two
# instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose
# price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.
class Bike:
    def __init__(self, a, b):
        self.color = a
        self.price = b


testOne = Bike('blue', 89.99)
testTwo = Bike('purple', 25.0)

# (NO.2)
# Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a
# number representing a quantity of apples. The constructor should initialize two instance variables: apple_color
# and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked.
# You should also write a __str__ method for this class that returns a string of the format: "A basket of
# [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples."
# (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)

class AppleBasket:
    def __init__(self, a, b):
        self.apple_color = a
        self.apple_quantity = b

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)


a1 = AppleBasket('Green', 50)
a2 = AppleBasket('Red', 50)
print(a1.increase())
print(a2)


# (No.3)
# Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and
# an integer that represents the amount of money in the account. The constructor should initialize two instance
# variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount,
# you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with
# "Bob" as the name and 100 as the amount. Save this to the variable t1.
class BankAccount:
    def __init__(self, a, b):
        self.name = a
        self.amt = b

    def __str__(self):
        return "Your account, {}, has {} dollars.".format(self.name,self.amt)

t1 = BankAccount('Bob', 100)
print(t1)