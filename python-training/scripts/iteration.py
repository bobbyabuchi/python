import math
"""
ITERATION - from thinkCSpy
"""
a6 = "6.1 - Multiple assignment"
b6 = "6.2 - The while statement"
c6 = "6.3 - Tables"
d6 = "6.4 - 2D tables"
e6 = "6.5 - Encapsulation and generalization"
f6 = "6.6 - More encapsulation"
g6 = "6.7 - Local variables"
h6 = "6.8 - More generalization"
i6 = "6.9 - Functions"
j6 = "6.10 - Glossary"
k6 = "..........................................................."

print (a6, k6)#6.1 - multiple assignment

# a new assignment makes an existing variable
ezk = 18
print (ezk),
ezk = 20
print (ezk)
ezk = 28
print (ezk)

print (b6, k6) #6.2 - the while statement

def countdown(n):
	while n > 5:
		print (n)
		n = n-1
	print ("Blastoff!")

print (c6,k6)#6.3 - tables

x = 1.0
while x < 10.0:
	print (x), '\t', math.log(x)
	x = x + 1.0

print (d6,k6)

i = 1
while i <= 6:
        print (2*i, '  '),
        i = i + 1
print (\n)
