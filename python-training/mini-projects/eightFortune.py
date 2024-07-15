import random

#name = input("What is your name? ")
name = "Vesta"
question = "Is coming out here to work a good idea?"
answer = ""

random_number = random.randint(1,9)
# print(random_number)

# assign a value to name by default, someone does not provide name 
if name == "":
  name = "Question: "

# Gen a random number 1-9 inclusive of 1 and 9

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

print(name, "asks:", question)
print("Maic 8-ball's answer: ", answer)
