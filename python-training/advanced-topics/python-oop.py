#!/usr/bin/env python3

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