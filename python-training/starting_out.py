# Age calculator
year_of_birth = int(input('Enter year of birth: '))
current_year = int(input('Enter current year: '))
age = current_year - year_of_birth
print(age)


# Calculate Hourly Pay-rate
hours_worked = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter pay rate: '))
print('One day:',hours_worked * pay_rate)
# hourly pay for a period of one month
monthly_working_days = 20
print('One Month: ',pay_rate * monthly_working_days)
annual_pay = monthly_working_days * pay_rate
print('Annually:',annual_pay * 12)


def annualPay():
    # Calculate Annual Pay
    name = input("Enter Name: ")
    monthly_pay = int(input('Enter monthly pay: '))
    return monthly_pay * 12

# CONSTANTS
PI = 3.14
NYOI = 1960
MOB = 'July'

# VARIABLES
fruit1 = 'Orange'
fruit2 = 'Apple'
fruit3 = 'Banana'

username = 'Tochukwu'
email = 'tochukwu@tech.com'
weight = 80
print(username)

user = ['Tochukwu', 'tochukwu@tech.com', 80]
print(user[0])

user_dict = {'name':'Tochukwu', 'email':'tochukwu@tech.com', 'weight':80}
print(user_dict['name'])

print(fruit1)

# LISTS
print(fruit1,fruit2,fruit3)

fruits = ['Orange', 'Apple', 'Banana']
print(fruits)
print(fruits[1])
print(fruits[0])

# TUPLES
fruits = ('Orange', 'Apple', 'Banana')

# BOOLEAN
a = True
b = False

if fruit1 == fruit2:
    print(a)
else:
    print(False)

2x2 = 4

print('Your annual pay is:', annual_pay)

# using recursive function---------------------------------------------------------------------------------
def factorial(number):
    return 1 if (number == 1 or number == 0) else number * factorial(number - 1)


print(factorial(5))

# Using a while loop----------------------------------------------------------------------------------------
num = int(input('Enter number: '))
fact = 1  # define factorial limit to positive numbers
g = 1  # initialise loop variable
if num < 0:
    print('cannot find factorial for a negative number!')
else:
    while g <= num:
        fact *= g
        g += 1
    print('{}{}'.format(num, f))


def x5(a):
    return a * x5(a - 1)


print(x5(5) - 5)

print(bob(2))

# code...
L = []
for a in range(5 + 1):
    # print(a+1)
    L.append(a)
for a in L:
    a = str(a)
print(L)
