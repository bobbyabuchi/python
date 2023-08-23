# Factorial
# 5 as input should display: 5! = 5x4x3x2x1 = 120

# code...get number from user
x = int(input('Enter number: '))
# code...initialise variables
n = []
m = ''
# code...package as a list and reverse the order
for a in range(1, x+1):
    n.append(a)                     # extract all the numbers in x and store in n
n.reverse()                         # put them in a reverse order

for b in n:                         # convert all them to string
    b = str(b)                      # "
    m += 'x'
    m += b  # m.join(b)             # package them in m
print(m)
l = len(m)                          # get the length of characters store as numerical value
for a in range(1, l):               #

    print(a)
print(m)


l = len(m)
for range in l:
    m += 'x'
print(m)

h = ['a', 'b', 'c']
i = [1, 2, 3]
str1 = ""
for ele in i:
    str1 += ele
print(str1)

# Driver code
s = ['Geeks', 'for', 'Geeks']
print(listToString(s))

for b in n:
    for d in b:
        print('hello!')

print(n, sep='x')
acc = 1
for a in n:
    acc *= a
    #n.append('x')
print(n)
    print(a, 'x', acc, sep='')

# Accumulator variable
numbers = [1, 2, 3, 4, 5, 6, 7]
acc = 0
for a in numbers:
    acc += a
print(acc)
