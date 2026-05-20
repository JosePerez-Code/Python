counter = 1

while counter <= 100:
    if counter % 7 == 0:
        print("I found it")
        break
    print(counter)
    counter = counter + 1
