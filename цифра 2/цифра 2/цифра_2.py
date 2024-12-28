n=input()
for i in n:
    if i in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')