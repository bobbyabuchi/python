# BroCode

credit = "5533-4657-3434-3344"

print(credit[:3]) # last three digits
print(credit[3:]) # omit first three digits
print(credit[::3]) # last six digits
print(credit[3::]) # omit first three digits

# shopping cart in Euro € --------------------------------------------------

items = []
total = []

while True:
    item = input("Enter item name: ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {item}: "))
        items.append(item)
        total.append(price)

print("------------Your Invoice ----------------")

for item, price in zip(items, total):
    print(f"[{item}, €{price}]", end="/ ")
print()

total = sum(total)

print(f"Total due is: €{total}")
print("------------------------------------")

# Quiz ------------------------------------------------------------------

questions = (
    "What is the capital of China?",
    "What is the capital of Burkina Faso?",
    "What is the capital of NewZealand?",
    "What is the capital of Russia?",
    "What is the capital of Ireland?",
)

options = (
    ("A. Shanghai", "B. Guangzhou", "C. Beijing"),
    ("A. Ouagadougou", "B. Banfora", "C. Kaya"),
    ("A. Wellington", "B. Auckland", "C. Christchurch"),
    ("A. Moscow", "B. Volgograd", "C. Omsk"),
    ("A. Dublin", "B. Athlone", "C. Johnstown")
)

answers = ("C", "A", "B", "A", "A")

guesses = []
score = 0
question_number = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Choose A, B or C : ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print(f" {guess} is correct!")
    else:
        print(f" {guess} is incorrect!")
        print(f"The correct answer is {answers[question_number]}!")
    question_number += 1

print("-------------------------------------")
print("------------- Results ---------------")
print("-------------------------------------")

print("Correct Answers..: ", end="")
for answer in answers:
    print(answer, end=" | ")
print()

print("Your Answers.....: ", end="")
for guess in guesses:
    print(guess, end=" | ")
print()

score_percentage = int(score / len(questions) * 100)
print(f"You scored {score}/{len(questions)}, {score_percentage}%")
print("-------------------------------------")