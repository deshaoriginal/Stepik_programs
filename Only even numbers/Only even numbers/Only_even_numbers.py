even_count = 0  # счетчик четных чисел

# считываем 10 чисел и проверяем каждое на четность
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        even_count += 1

# если количество четных чисел равно 10, то все числа четные, иначе - нет
if even_count == 10:
    print("YES")
else:
    print("NO")
    
