name = input("Enter your name: ").lower().strip()
password = int(input("Choose a number (1/2/3): "))
years = int(input("Enter years worked: "))

if password == 1:
    if years == 1:
        print("You have 6 vacation days.")
    elif years >= 2 and years <= 6:
        print("You have 14 vacation days.")
    elif years >= 7:
        print("You have 20 vacation days.")
    else:
        print("Invalid years.")

elif password == 2:
    if years == 1:
        print("You have 7 vacation days.")
    elif years >= 2 and years <= 6:
        print("You have 15 vacation days.")
    elif years >= 7:
        print("You have 22 vacation days.")
    else:
        print("Invalid years.")

elif password == 3:
    if years == 1:
        print("You have 10 vacation days.")
    elif years >= 2 and years <= 6:
        print("You have 20 vacation days.")
    elif years >= 7:
        print("You have 30 vacation days.")
    else:
        print("Invalid years.")

else:
    print("Invalid key, no vacation days assigned.")
