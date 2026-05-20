# If temperature is 38 or higher:
#   Ask if the user has a headache
#   If yes → "Possible fever"
#   If no → "Observation recommended"
# If temperature is lower than 38:
#   Print: "Normal temperature"

temperature = int(input("Enter your temperature: "))

if temperature >= 38:
    headache = input("Do you have a headache? (yes/no): ").strip().lower()

    if headache == "yes":
        print("Possible fever")
    elif headache == "no":
        print("Observation recommended")
    else:
        print("Invalid input")
else:
    print("Normal temperature")
