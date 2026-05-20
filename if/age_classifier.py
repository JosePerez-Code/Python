# 1. Ask the user for their name
# 2. Ask the user for their age
# 3. Use conditionals to show:
# 0 to 12 → "You are a child"
# 13 to 17 → "You are a teenager"
# 18 or more → "You are an adult"
# 4. At the end print: "User: X — Age: Y"

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <= 12:
    print("You are a child")
elif age <= 17:
    print("You are a teenager")
else:
    print("You are an adult")

print(f"User: {name} Age: {age}")
