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
