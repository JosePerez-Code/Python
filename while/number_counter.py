# 1. Print numbers from 1 to 10.
# 2. Print numbers from 10 to 1 (reversed).
# 3. Ask user for a number and print its multiplication table.
# 4. Ask user for a password. Keep asking if wrong.
#    Password: python123

password = input("Password: ")

while password != "python123":
    print("Incorrect Password")
    password = input("Password: ")

print("Correct Password")
