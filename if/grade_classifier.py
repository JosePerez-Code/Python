# 1. Ask the user for their name
# 2. Ask the user for their grade (0 to 100)
# 3. Use conditionals to classify the grade:
# 90 or more → "Excellent"
# 70 to 89 → "Passed"
# 0 to 69 → "Failed"
# 4. If the name is "Jose", print a special message
# 5. At the end, print: "Your final grade is: X"

while True:
    try:
        name = input("Enter your username: ")
        grade = int(input("Enter your grade (0-100): "))

        if grade < 0 or grade > 100:
            print("Error: grade must be between 0 and 100")
        else:
            if name.lower() == "jose":
                print("Welcome back, Jose. Let's see your result.")

            if grade >= 90:
                print("Excellent")
            elif grade >= 70:
                print("Passed")
            else:
                print("Failed")

            print(f"Your final grade {name} is {grade}")
            break
    except ValueError:
        print("Error, porfavor use numeros.") 