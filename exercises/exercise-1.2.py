text = input("Enter your text: ")
words = text.split(" ")
total = len(words)

if total > 120:
    print("para bro no me digas un testamento")

print(f"dijiste esta cantidad de palabras {total} y durarias {total / 2} segundo en decirlas")
print(f"dalto diria esta misma cantidad de palabras en {total / 2 / 1.3 } segundos")

