# 1. Ask for the user's name
# 2. Ask for their city
# 3. Ask for the current temperature
# 4. Use conditionals:
# 30 or more → "It is very hot"
# 15 to 29 → "The weather is nice"
# less than 15 → "It is cold"
# 5. At the end print: "User X — City Y — Temperature Z"

name = input("Enter your name: ")
city = input("Enter your city: ")
temperature = int(input("Enter the current temperature (numbers only): "))

if temperature >= 30:
    print("It is very hot")
elif temperature >= 15:
    print("The weather is nice")
else:
    print("It is cold")

print(f"User: {name} - City: {city} - Temperature: {temperature}°C")
