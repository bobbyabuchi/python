# working with LIST 06.07.24
result = [["development", 80], ["administration", 96], ["data engineering", 97], ["architecture", 65]]

# Reference item in a 2D list eg. latin score
latinScore = result[1][1]

# modify item in 2D list architecture score
result[3][1] = 95

# add item to list...package a sublist in var and append as in 1D list
techSupport = ["tech support", 88]
result.append(techSupport)

# modify visual art score (being the last in, -1 index will do)
result[-1][-1] = 98

# Range
goodRange = range(2, 1001, 10) # 2 is the first digit, 1000 is the max , 10 is the diff

# Negative indices can take all but n last elements of a list.
suitcase = ["laptop", "power adapter", "mouse", "flash drive", "WiFi Router", "iPhone"]
last_two_elements = suitcase[-2:]
slice_off_last_three = suitcase[:-3]

# WORKING WITH LISTS IN PYTHON -- Review
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10,"19th Century Bed Frame")
inventory.sort()

inventory_len = len(inventory)

print(removed_item)
# outputs...
print(latinScore) # 96
print(result)
# print(editedResult)
print(list(goodRange))

# date: 9.7.24

# Len's Slice: organize some of your sales data

toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovias"],
  [2, "mushrooms"],
]

# Sort in the order of increasing price (asc)
pizza_and_prices = sorted(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

# most expensive sold
pizza_and_prices.pop() 

# add new product
newPizaa = [2.5,"peppers"]
pizza_and_prices = pizza_and_prices + newPizaa

# get the three cheapest pizza
three_cheapest = pizza_and_prices[:3]

# print(num_two_dollar_slices)
# print(num_pizzas)
print("We sell",num_pizzas,"different kinds of pizza!\n")
print(pizza_and_prices,"\n")
print(priciest_pizza,cheapest_pizza,"\n")
print(three_cheapest,"\n")

# 13.07.2024

promise = "I will finish the python loops module!"

# to use range function with for loop, you can either 

for x in range(0,5):
  print(promise)
# or simply...
for x in range(5):
  print(promise)

# use while loop to print the elements of a list 
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0

while index < length:
  print("I am learning about",python_topics[index])
  index += 1

# use break statement to stop a loop when condition is met
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for x in location:
    scoops_sold += x
print(scoops_sold)

# list comprehension
# syntax: new_list = [<expression> for <element> in <collection>]

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [x + 10 for x in grades]
print(scaled_grades)

# create a new list can_ride_coaster that has every element from heights > 161.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [x for x in heights if x > 161]
print(can_ride_coaster)

# list review
single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
for x in single_digits:
  print(x)
  # append the squared value of each element of single_digits
  squares.append(x**2)
print(squares)
# element of single_digits taken to the third power
cubes = [x**3 for x in single_digits]
print(cubes)

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# sum the price list method 1
total_price = sum(prices)
print(total_price)
# sum up price list method 2
tp = 0
for x in prices:
  tp += x
print(tp)
# get avg price
average_price = total_price/(len(prices))
print("Average Haircut Price:",average_price)
# make a list new prices -5
new_prices = [each_item - 5 for each_item in prices]
print(new_prices)

# ............... 14.07.24........................
# Import random below:
import random

# Create random_list of 101 random numbers:
random_list = [random.randint(1,100) for i in range(101)]

# pick a random number from the random list:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

# Object Oriented Python............................ 15.07.24................................. 

# create a class Rules
class Rules:
  # define a method(function within a class)
  def washing_brushes(self): # self by convention
    # return a value( a string here....)
    return "Point bristles towards the basin while washing your brushes."

# class method with argument...
class Circle:
  pi = 3.14
  def area(self, radius):
    # ref a vaiable in the class outside the method -> Classname.variablename
    return Circle.pi * radius ** 2

# instances of Circle class
# ref a method -> Classname.method() ... given the diameter 12, 36 and 11460 find area
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
