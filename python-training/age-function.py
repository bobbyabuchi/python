# import datetime
import datetime

# get cuttent datetime from datetime library
t = datetime.datetime.now()

current_year = t.year
username = input('Enter Name: ')
year_of_birth = input("Enter Year of Birth: ")
year_of_birth = int(year_of_birth)
age = current_year - year_of_birth
if age >= 18:
    flash_message = "{} you are {} and eligible, kindly apply."
    print(flash_message.format(username,age))
else:
    flash_message = "You are {} and not eligible for the job."
    print(flash_message.format(age))

def ageCal(name, age):
    pass

ageCal()

# import datetime
import datetime

# get cuttent datetime from datetime library
t = datetime.datetime.now()

current_year = t.year
username = input('Enter Name: ')
year_of_birth = input("Enter Year of Birth: ")
year_of_birth = int(year_of_birth)
age = current_year - year_of_birth
if age >= 18:
    flash_message = "{} you are {} and eligible, kindly apply."
    print(flash_message.format(username,age))
else:
    flash_message = "You are {} and not eligible for the job."
    print(flash_message.format(age))