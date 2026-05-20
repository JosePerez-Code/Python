account_active = True
book_available = False
book_overdue = True

if account_active == True:
    if book_overdue == False:
        if book_available == True:
            print("You can take the book")
        else:
            print("The book is not available, choose another one")
    else:
        print("You have overdue books, please return them first")
else:
    print("Your account is not active")
