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

#TODO: class methods and members
class eBbook:
    
#TODO:
#TODO:
