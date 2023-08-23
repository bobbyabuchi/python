import datetime  # import datetime

# get current datetime from datetime library
t = datetime.datetime.now()
current_year = t.year  # get only the year

username = input('Enter Name: ')
year_of_birth = input("Enter Year of Birth: ")
year_of_birth = int(year_of_birth)
age = current_year - year_of_birth
if age > 18:
    flash_message = "{} you are {} and eligible, kindly apply."
    print(flash_message.format(username,age))
else:
    ok_year = 18 - age
    ok_year = current_year + ok_year
    flash_message = "You are {} and not eligible, for the job now, apply in {}."
    print(flash_message.format(age, ok_year))