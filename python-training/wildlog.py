"""
https://www.w3schools.com/python Review
"""
# Python Strings

a = "Bobby"
print(a)
print(a[:3])
print(a[-2:])
print(a[:3]+a[-2:])

s1 = " I love you. "
s2 = s1.strip() # remove any whitespace from the beginning or the end
print(s1)
print(s2)

s = "I love you."
print(s.lower())
print(s.replace('you', 'Chisom'))
print(s.split())

txt = "The rain in Spain stays mainly in the plain"
x = "ain"
if x in txt:
    print(True)
else:
    print(False)

# alternatively
#x = "ain" not in txt
print(x)

# we can combine strings and numbers by using the format()
modules = 5
specialization = 'Python 3 Specialization'
price = 49.00
sentence = "I am taking {} of {} modules at the price of {} dollars/month."
print(sentence.format(specialization, modules, price))
# we can index to swap the position of varaibles or ensure right order of output
sentence = "I am taking {2} of {1} modules at the price of {0} dollars/month."
print(sentence.format(specialization, modules, price))

# Using Hex Value
nameHex = "\x42\x6f\x62\x62\x79"
print(nameHex)

"""
Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored.
"""
x = input("Enter a sentence")

x = x.lower()   # convert to all lowercase

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in x:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])

"""
Write a program that finds the most used 7 letter word in scarlet3.txt.
"""
f = open('scarlet3.txt', 'r')
contents = f.read()
d = {}

for w in contents.split():
    if len(w) == 7:
        if w not in d:
            d[w] = 1
        else:
            d[w] = d[w] + 1

dkeys = d.keys()
most_used = dkeys[0]
for k in dkeys:
    if d[k] > d[most_used]:
        most_used = k

print("The most used word is '"+most_used+"', which is used "+str(d[most_used])+" times")

# draw an equilateral triangle
import turtle

wn = turtle.Screen()
norvig = turtle.Turtle()

for i in range(3):
    norvig.forward(100)

    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    norvig.left(360/3)

wn.exitonclick()

# a star
import turtle

turing = turtle.Turtle()

for i in range(5):
    turing.forward(110)
    turing.left(216)

# Write a program to draw some kind of picture. Be creative and experiment with the turtle methods.
import turtle

tanenbaum = turtle.Turtle()

tanenbaum.hideturtle()
tanenbaum.speed(20)

for i in range(350):
    tanenbaum.forward(i)
    tanenbaum.right(98)


"""
In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.

Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?
"""

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)

print(bool("Hello"))
print(bool(15))

import math

class Point:
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

    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(4,3)
q = Point(0,0)
print(p.distance(q))


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
        return "{}, is produced by {} and has {} grams of fiber in every serving!".format(self.n, self.b, self.f)


c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)