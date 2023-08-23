D1 = 0.10  # for 1 litre or less
D2 = 0.25  # for more than 1 litre

d1_bottles = float(input('Enter number of bottles 1 litre or less: '))
d2_bottles = float(input('Enter number of bottles more than 1 litres: '))
#  float(d1_bottles, d2_bottles)
name = input('your name: ')
balance = (d1_bottles * 0.10) + (d2_bottles * 0.25)
#  result = format(balance, '.2f')
print('$', format(balance, '.2f'), sep='')

print('{} Your balance is ${}'.format(name, format(balance, '.2f')))
print("-----------------------------------------------")

#  print('colors:', 'red', 'green', 'blue', sep='+')

print("Please input your name")
name = input(str())
print("input your date of birth")
DOB = input()

print("{} you were born in {}".format(name, DOB))