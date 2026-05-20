name = input("Enter your username: ")

print("1. See personalized greeting")
print("2. Even or odd")
print("3. Recommendation by hour")
print("4. Exit")

option = int(input("Choose an option: "))

if option == 1:
    print(f"Hello, {name}. I hope you are having a great day.")

elif option == 2:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

elif option == 3:
    hour = int(input("Enter the time (0-23): "))
    if hour >= 0 and hour <= 11:
        print("Good morning")
    elif hour >= 12 and hour <= 17:
        print("Good afternoon")
    elif hour >= 18 and hour <= 23:
        print("Good evening")
    else:
        print("Invalid time")

elif option == 4:
    print("Exiting the program...")

else:
    print("Invalid option")
