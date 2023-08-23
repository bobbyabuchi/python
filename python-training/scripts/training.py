import datetime

# (1) Write a program that asks the user to enter his or her name. The program should
# respond with a message that says hello to the user, using his or her name.

name = input("Please enter your name: ")
print("Hello {}!".format(name))

# (2) Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with

# read the input values from user
length = float(input("Enter length of room in feet: "))
width = float(input("Enter width of room in feet: "))

area = length * width
print("The are of the room is {} square feet".format(area))

# (3) Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

SQFT_PER_ACRE = 43560

length = float(input("Enter the length of field in feet: "))
width = float(input("Enter the width of field in feet: "))

area = length * width

acres = length * width / SQFT_PER_ACRE
print("The area of the field {} = {} acres".format(area, acres))

name = "Nonso"
print(name)
print(name.upper())

# (4) In many shops a small deposit is added to drink containers to encourage people
# to return them. In one particular shop, drink containers holding one liter or
# less have a 10.00 NGN deposit, and drink containers holding more than one liter have a
# 25.00 NGN deposit. Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a NGN (Nigerian Naira) and always displays exactly two decimal places.

LESS_DEPOSIT = 10
MORE_DEPOSIT = 25

less = int(input("How many containers 1 litre or less do you have? "))
more = int(input("How many containers more than 1 litre do you have? "))

refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

print("Your total refund will be NGN{}.".format(refund))

# (5) Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula: sum = ((n)(n + 1))/2

n = int(input("Enter a positive integer: "))
int_sum = n * (n+1) / 2
print("The sum of the first {} positive integers is {}".format(n,int_sum))

# (6) An online retailer sells two products: gold cubes and platinum cubes. One cube of gold weighs 80
# grams. One cube of platinum weighs 120 grams. Write a program that reads the number of
# gold and the number of platinum in an order from the user. Then your program
# should compute and display the total weight of the order.

WEIGHT_OF_GOLD_CUBE = 80 # grams
WEIGHT_OF_PLATINUM = 120 # grams

gold_qty = int(input("Enter number of gold ordered: "))
platinum_qty = int(input("Enter number of platinum ordered: "))

total_weight_ordered = (gold_qty * 80) + (platinum_qty * 120)

print("The total weigth of goods ordered is {} grams.".format(total_weight_ordered))

# (7) Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

INTEREST = 4/100 # 4%

amount_deposited = float(input("Amount deposited: "))
year1 = amount_deposited + ((amount_deposited * INTEREST) * 1)
year2 = amount_deposited + ((amount_deposited * INTEREST) * 2)
year3 = amount_deposited + ((amount_deposited * INTEREST) * 3)

print(format(year1, '.2f'))
print(format(year2, '.2f'))
print(format(year3, '.2f'))


# (8) Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b

a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

print("Sum of the two integers = ", a + b)
print("Difference of the two integers = ", a - b)
print("Product of the two integers = ", a * b)

# (9) In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

feet = float(input("Enter value in feet: "))
inches = feet * 12
yards = feet / 3
miles = feet / 5280
print(feet,"feet to inches is",inches)
print(feet,"feet to yards is",yards)
print(feet,"feet to miles is",miles) 

# (10) Python includes a library of functions for working with time, including a function
# called asctime in the time module. It reads the current time from the com-
# puter’s internal clock and returns it in a human-readable format. Write a program
# that displays the current time and date. Your program will not require any input from
# the user.

t = datetime.datetime.now()
print(t)

h = t.strftime("%I")
m = t.strftime("%M")
s = t.strftime("%S")
p = t.strftime("%p")
date = t.strftime("%d")
month = t.strftime("%B")
y = t.strftime("%Y")

print("It is {} {}, {} and the time is {}:{}:{}:{}.".format(month,date,y,h,m,s,p))