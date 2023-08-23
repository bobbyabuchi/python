"""
- Now no chastening for the present seemeth to be joyous, but grievous:
nevertheless afterward it yieldeth the peaceable fruit of righteousness unto them which are exercised thereby.
- Wherefore lift up the hands which hang down, and the feeble knees;
- And make straight paths for your feet, lest that which is lame be turned out of the way; but let it rather be healed.
- Follow peace with all men, and holiness (treat all men with love & respect), without which no man shall see the Lord:
Hebrews 12:11-14 @Ecclus.12**1->4/||@|
"""
# Code here...

L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [a+b for (a,b) in list(zip(L1,L2)) if a > 10 if b < 5]
print (L3)



____________________________________________________________________
____________________________________________________________________
# Write to file...
txt_file = open("I:/pydata/h1211.csv", "w")
txt_file.write("Name,Phone,Email")
txt_file.write('\n')
txt_file.write("Bob,080,b@p.com.ng")
txt_file.close()
txt_file = open("I:/pydata/h1211.csv", "r")
content = txt_file.readlines()
print(content)
txt_file.close()

# Project [Generate Multiplication (2x to 12x) Table with Code]
list_num = list(range(1, 13))
def m_table():
    count = 0
    f = open("I:/pydata/m_table.txt", "w")
    for num in list_num:
        mul = a * num
        count += 1
        print(a, " x ", count, " = ", mul)
        f.write(str(a), "x", str(count), " = ", str(mul) + "\n")
    f.close()
a = 2
m_table()
____________________________________________________________________
____________________________________________________________________
# Python String join() Method
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("Chima", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("Chima", "Peter", "Vicky")
x = ",".join(myTuple)
print(x)





# A machine learning engineer is a full-blown software engineer (and hardcore programmer) that has specialised
# in machine learning. The length and breadth of skills you need to excel in the real world will take years to master.
# The learning curve is brutal so do not relent.

