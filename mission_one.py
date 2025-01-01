# BroCode

credit = "5533-4657-3434-3344"

print(credit[:3]) # last three digits
print(credit[3:]) # omit first three digits
print(credit[::3]) # last six digits
print(credit[3::]) # omit first three digits

# shopping cart in Euro €

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