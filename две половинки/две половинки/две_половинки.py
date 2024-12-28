
text = input("Введите строку текста: ")

length = len(text)
half_length = length // 2

if length % 2 == 1:  # Если длина строки нечетная
    half_length += 1

first_half = text[:half_length]
second_half = text[half_length:]

rearranged_text = second_half + first_half
print("Переставленная строка:", rearranged_text)
