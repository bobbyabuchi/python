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

