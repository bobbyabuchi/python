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

# outputs...
print(latinScore) # 96
print(result)
# print(editedResult)
