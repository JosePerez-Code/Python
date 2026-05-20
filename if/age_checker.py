# Ask the user for their age.
# If age is under 18, show: "You are a minor."
# If age is 18 or older, show: "You are an adult."
# If age is negative, show: "Invalid age."

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif age >= 0:
    print("You are a minor")
else:
    print("Invalid age")
