number = int(input())
lastdigit = number % 10  # последняя цифра числа
digit3count = 0  # количество цифр 3
lastdigitcount = 0  # количество раз, которое встречается последняя цифра
evendigitcount = 0  # количество четных цифр
sumgreaterthan5 = 0  # сумма цифр, больших пяти
productgreaterthan7 = 1  # произведение цифр, больших семи
zeroor5count = 0  # количество цифр 0 и 5

while number > 0:
    digit = number % 10
    if digit == 3:
        digit3count += 1
    if digit == lastdigit:
        lastdigitcount += 1
    if digit % 2 == 0:
        evendigitcount += 1
    if digit > 5:
        sumgreaterthan5 += digit
    if digit > 7:
        productgreaterthan7 *= digit
    elif digit > 7:
        productgreaterthan7 = digit
    if digit == 0 or digit == 5:
        zeroor5count += 1
    number //= 10

print(digit3count)
print(lastdigitcount)
print(evendigitcount)
print(sumgreaterthan5)
print(productgreaterthan7)
print(zeroor5count)