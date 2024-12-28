text = input("Введите строку: ")
count = 0

for char in text:
    if char.islower():
        count += 1

print("Количество буквенных символов в нижнем регистре:", count)
