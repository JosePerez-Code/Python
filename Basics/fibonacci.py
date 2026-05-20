number_1 = 0
number_2 = 1
result = 0
counter = 1

while counter <= 10:
    print(number_1, number_2, end=" ")
    result = number_1 + number_2
    number_1 = result
    number_2 = result + number_2
    counter = counter + 1
