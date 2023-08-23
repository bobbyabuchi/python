#!/usr/bin/env python3

# OBJECT ORIENTED PROGRAMING WITH PYTHON ---------------------------------------------------------

# Classes and Inheritance (Week 1) ----------------------------------------------------------------------------

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

# Classes and Inheritance (Week 2) ----------------------------------------------------------------------------

# 22.1. Introduction: Class Inheritance

'''
Consider our Tamagotchi game. Suppose we wanted to make some different kinds of pets that have the same structure as
other pets, but have some different attributes or behave a little differently. For example, suppose that dog pets
should show their emotional state a little differently than cats or act differently when they are hungry or when they
are asked to fetch something.

You could implement this by making an instance variable for the pet type and dispatching on that instance variable in
various methods.
'''

from random import randrange


class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Boom Boom Boom']

    def __init__(self, name="Kitty", pet_type="dog"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class
        self.pet_type = pet_type

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            if self.pet_type == "dog": # if the pet is a dog, it will express its mood in different ways from a cat or any other type of animal
                return "happy"
            elif self.pet_type == "cat":
                return "happy, probably"
            else:
                return "HAPPY"
        elif self.hunger > self.hunger_threshold:
            if self.pet_type == "dog": # same for hunger -- dogs and cats will express their hunger a little bit differently in this version of the class definition
                return "hungry, arf"
            elif self.pet_type == "cat":
                return "hungry, meeeeow"
            else:
                return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)


# 22.2. Inheriting Variables and Methods

'''
Inheritance provides us with an easy and elegant way to represent these differences. 
In the definition of the inherited class, you only need to specify the methods and instance variables that are 
different from the parent class (the parent class, or the superclass, is what we may call the class that is inherited 
from.

Here is an example. Say we want to define a class Cat that inherits from Pet. Assume we have the Pet class that we 
defined earlier.

We want the Cat type to be exactly the same as Pet, except we want the sound cats to start out knowing “meow” instead 
of “mrrp”, and we want the Cat class to have its own special method called chasing_rats, which only Cat s have.

We do that by putting the word Pet in parentheses, class Cat(Pet):
'''
#------------- refer to the code above------------------------------append this to it.......
p1 = Pet("Fido")
print(p1) # we've seen this stuff before!

p1.feed()
p1.hi()
print(p1)

cat1 = Cat("Fluffy")
print(cat1) # this uses the same __str__ method as the Pets do

cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi()
print(cat1)

print(cat1.chasing_rats())

#print(p1.chasing_rats()) # This line will give us an error. The Pet class doesn't have this method!

'''
And you can continue the inheritance tree. We inherited Cat from Pet. Now say we want a subclass of Cat called 
Cheshire. A Cheshire cat should inherit everything from Cat, which means it inherits everything that Cat inherits 
from Pet, too. But the Cheshire class has its own special method, smile.
'''

class Cheshire(Cat): # this inherits from Cat, which inherits from Pet

    def smile(self): # this method is specific to instances of Cheshire
        print(":D :D :D")

# Let's try it with instances.
cat1 = Cat("Fluffy")
cat1.feed() # Totally fine, because the cat class inherits from the Pet class!
cat1.hi() # Uses the special Cat hello.
print(cat1)

print(cat1.chasing_rats())

new_cat = Cheshire("Pumpkin") # create a Cheshire cat instance with name "Pumpkin"
new_cat.hi() # same as Cat!
new_cat.chasing_rats() # OK, because Cheshire inherits from Cat
new_cat.smile() # Only for Cheshire instances (and any classes that you make inherit from Cheshire)

# cat1.smile() # This line would give you an error, because the Cat class does not have this method!

# None of the subclass methods can be used on the parent class, though.
p1 = Pet("Teddy")
p1.hi() # just the regular Pet hello
#p1.chasing_rats() # This will give you an error -- this method doesn't exist on instances of the Pet class.
#p1.smile() # This will give you an error, too. This method does not exist on instances of the Pet class.


# intro-9-2: What would print after running the following code:
new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
another_cat.song()
# -> We are Siamese if you please. We are Siamese if you don’t please.
# another_cat is an instance of Siamese, so its song() method is invoked.

# intro-9-3: What would print after running the following code:
new_cat = Cheshire("Pumpkin”)
class Siamese(Cat):
  def song(self):
    print("We are Siamese if you please. We are Siamese if you don’t please.")
another_cat = Siamese("Lady")
new_cat.song()
# -> Error
# You cannot invoke methods defined in the Siamese class on an instance of the Cheshire class. Both are subclasses
# of Cat, but Cheshire is not a subclass of Siamese, so it doesn't inherit its methods.

# 22.3. Overriding Methods

# Here’s the original Pet class again.

from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

'''
Now let’s make two subclasses, Dog and Cat. Dogs are always happy unless they are bored and hungry. Cats, on the other 
hand, are happy only if they are fed and if their boredom level is in a narrow range and, even then, only with 
probability 1/2.
'''

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

c1 = Cat("Fluffy")
d1 = Dog("Astro")

c1.boredom = 1
print(c1.mood())
c1.boredom = 3
for i in range(10):
    print(c1.mood())
print(d1.mood())

# 22.4. Invoking the Parent Class’s Method

# when the parent class has a useful method, but you just need to execute a little extra code when running the
# subclass’s method

#...refer to the Pets Class again, then see append code below

from random import randrange

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

d1 = Dog("Astro")

d1.feed()


# a better way to invoke a superclass’s method

'''
Let’s say we want to create a subclass of Pet, called Bird, and we want it to take an extra parameter, chirp_number, 
with a default value of 2, and have an extra instance variable, self.chirp_number. Then, we’ll use this in the hi 
method to make more than one sound.
'''

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        super().__init__(name)
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

b1 = Bird('tweety', 5)
b1.teach("Polly wanna cracker")
b1.hi()


# 22.5. Tamagotchi Revisited

'''
Using what we know about class inheritance, we can make a new version of the Tamagotchi game, where you can adopt 
different types of pets that are slightly different from one another.

And now we can play the Tamagotchi game with some small changes, such that we can adopt different types of pets. 
'''

import sys
sys.setExecutionLimit(60000)
from random import randrange

class Pet(object):
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.update_boredom()

    def feed(self):
        self.update_hunger()

    def update_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def update_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.update_boredom()

class Lab(Dog):
    def fetch(self):
        return "I found the tennis ball!"

    def hi(self):
        print(self.fetch())
        print(self.sounds[randrange(len(self.sounds))])

class Poodle(Dog):
    def dance(self):
        return "Dancin' in circles like poodles do."

    def hi(self):
        print(self.dance())
        Dog.hi(self)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
def whichtype(adopt_type="general pet"):
    return pet_types.get(adopt_type.lower(), Pet)

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                # figure out which class it should be
                if len(words) > 2:
                    Cl = whichtype(words[2])
                else:
                    Cl = Pet
                # Make an instance of that class and append it
                animals.append(Cl(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()

play()

#---------------------------- week 2 assessment -----------------------------------------------------

# Q1
'''
The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. 
An instance of the class is one pokemon that you create.

Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are 
different.

For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a 
lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to 
the variable p1.
'''


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)


p1 = Grass_Pokemon('Belle')

# Q2
'''
Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the attack_boost amount when they are trained.

To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable p2. Create another instance of the Grass_Pokemon class with the name set to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods to train the p3 Grass_Pokemon instance until it reaches at least level 10

'''

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"
    attack_boost = 10

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')


# Q4
'''
Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.

Grass is weak against Fire and strong against Water

Ghost is weak against Dark and strong against Psychic

Fire is weak against Water and strong against Grass

Flying is weak against Electric and strong against Fighting

For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')
'''


class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.ptype = None
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

    def opponent(self):
        if self.ptype == "Grass":
            return ("Fire", "Water")
        elif self.p_type == "Ghost":
            return ("Dark", "Psychic")
        elif self.p_type == "Fire":
            return ("Water", "Grass")
        else:
            return ("Electric", "Fighting")


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def opponent(self):
        if self.p_type == "Grass":
            return ("Fire", "Water")


class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3


class Fire_Pokemon(Pokemon):
    p_type = "Fire"

    def opponent(self):
        if self.p_type == "Fire":
            return ("Water", "Grass")


class Flying_Pokemon(Pokemon):
    p_type = "Flying"

    def opponent(self):
        if self.p_type == "Flying":
            return ("Electric", "Fighting")

# alternatively...?

    class Pokemon():
        attack = 12
        defense = 10
        health = 15
        p_type = "Normal"

        def __init__(self, name, level=5):
            self.name = name
            self.level = level
            self.weak = "Normal"
            self.strong = "Normal"

        def train(self):
            self.update()
            self.attack_up()
            self.defense_up()
            self.health_up()
            self.level = self.level + 1
            if self.level % self.evolve == 0:
                return self.level, "Evolved!"
            else:
                return self.level

        def attack_up(self):
            self.attack = self.attack + self.attack_boost
            return self.attack

        def defense_up(self):
            self.defense = self.defense + self.defense_boost
            return self.defense

        def health_up(self):
            self.health = self.health + self.health_boost
            return self.health

        def update(self):
            self.health_boost = 5
            self.attack_boost = 3
            self.defense_boost = 2
            self.evolve = 10

        def __str__(self):
            self.update()
            return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

        def opponent(self, p_type):
            if self.ptype == "Grass":
                return ("Fire", "Water")
            elif self.p_type == "Ghost":
                return ("Dark", "Psychic")
            elif self.p_type == "Fire":
                return ("Water", "Grass")
            else:
                return ("Electric", "Fighting")

        def opponent(self, p_type):

        if self.p_type == "Grass":
            return ("Fire", "Water")
        elif self.p_type == "Ghost":
            return ("Dark", "Psychic")
        elif self.p_type == "Fire":
            return ("Water", "Grass")
        else:
            return ("Electric", "Fighting")

    class Grass_Pokemon(Pokemon):
        attack = 15
        defense = 14
        health = 12
        p_type = "Grass"

        def update(self):
            self.health_boost = 6
            self.attack_boost = 2
            self.defense_boost = 3
            self.evolve = 12

        def opponent(self):
            if self.p_type == "Grass":
                return ("Fire", "Water")

    class Ghost_Pokemon(Pokemon):
        p_type = "Ghost"

        def update(self):
            self.health_boost = 3
            self.attack_boost = 4
            self.defense_boost = 3

        def opponent(self):
            if self.p_type == "Ghost":
                return ("Dark", "Psychic")

    class Fire_Pokemon(Pokemon):
        p_type = "Fire"

        def opponent(self):
            if self.p_type == "Fire":
                return ("Water", "Grass")

    class Flying_Pokemon(Pokemon):
        p_type = "Flying"

        def opponent(self):
            if self.p_type == "Flying":
                return ("Electric", "Fighting")

# Classes and Inheritance (Week 3) ----------------------------------------------------------------------------

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


# Keep your programs and code organised...with OOP -> Data/Atrribute+Function/Method

#todo: A basic class
class Book:
    # the 'init' called to create and initialise the instance of a class
    def __init__(self, title, author, pages, price):
        # class properties
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "this is a secret" #? just an underfined attribute to make a point
    #todo: an instance method
    def getprice(self):
        # check if attr is present/defined then run code
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount #? that other devs may now u can only access this from within the class

class Newspaper:
    def __init__(self, name):
        self.name = name

#todo: instance of the class
b1 = Book("No more two", "G.Akanni", 200, 20.22)
b2 = Book("Fulfilling MR", "G.Akanni", 120, 20.15)

# more instances of a class for comparing instance types
b3 = Book("Decree of the Watchers")
b4 = Book("Protocol of Sex")
n1 = Newspaper("Earth Angels")
n2 = Newspaper("Whispers of Love")

#todo: print class and property
print(b1)
print(b1.title)

#todo: pring price of books
print(b1.getprice())
print(b2.getprice())

# todo: set a discount
b2.setdiscount(0.5)
print(b2.getprice())

#todo: print secret attribute
print(b2.__secret) #? this will show an error because
print(b2._Book__secret) #? should work...though not a perfect solution

#TODO: check instance type
print(type(b3))
print(type(b4))
print(type(n1))
print(type(n2))

#TODO: compare two diff objects to see if same type
print(type(b3)) == (type(b4))
print(type(b3)) == (type(n1))

#TODO: use instance() to compare a specific instance...
print(isinstance(b3, Book))         #true
print(isinstance(n1, Newspaper))    #true
print(isinstance(n2, Book))         #false
print(isinstance(n2, object)) # check if it's an instance of object - TRUE for all python objects

# Write a class 
#   that calculates and stores the height and weight of a person in metric. 
#   The file should be named lab.py.  
#   BMI is calculated using this formula: Weight/Height^2 (kg and  m)
# The class should have two properties named:
#     Weight
#     Height
# The class should have two methods:
#     BMI_Value – This takes no arguments and returns a decimal value of the BMI
#     Equals – This should override the equals method from the object class to compare the weight and height of two BMI objects.  
#               To override the equal method you should implement this method: __eq__(self, other) and return a boolean


class BMI:
    def __init__(self, weight="", height=""):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / self.height ** 2

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

student1 = BMI(70, 76)
print(student1.BMI_Value())

# Constructor __init___ ----------------------------------------------------------------------

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())




