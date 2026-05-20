# Exercise: Purchase verification
# Rules:
# If under 18 → "You cannot make a purchase"
# If 18 or older:
#   If has card → "Purchase approved"
#   If not → "You need a card to make a purchase"

age = int(input("Enter your age: "))

if age >= 18:
    card = input("Do you have a card? (yes/no): ").strip().lower()

    if card == "yes":
        print("Purchase approved")
    elif card == "no":
        print("You cannot make a purchase, you need a card")
    else:
        print("Invalid input")
else:
    print("You are a minor, you cannot make a purchase")
