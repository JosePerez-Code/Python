# ATM Simulator
# Verify:
# If PIN is correct (1234)
# If amount is greater than 0
# If there is enough balance (available balance: 500)

while True:
    try:

        pin = int(input("Enter your pin: "))

        if pin == 1234:
            print("Correct Password")

            balance = int(input("Enter the amount you want to withdraw (Available balance $500): "))

            if balance >= 1 and balance <= 500:
                amount = (500 - balance)
                print(f"Your remaining balance is {amount}$")
                print(f"You have withdrawn {balance}$")
                break
            else:
                print("Invalid amount, must be between $1 and $500")
        else:
            print("Incorrect Password")
        
    except ValueError:
        print("Error, Ingrese un Numero valido")