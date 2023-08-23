# PYTHON DATA STRUCTURES......................................

# [start : end+1 : step]
x = "computer"

print(x[1:6:2])
print(x[1::3])
print(x[-4])
print(x[5])

# checking membership

a = "wisdom"
print("d" in a)
print("v" in a)

b = ['hope', 'faith', 'love']
print('pride' not in b)

c = ('hope', 'faith', 'love')
print('love' in c)

# iterate through items in a sequence

# list comprehension
a = [m for m in range(8)] # create a list of int 1-7
print(a)