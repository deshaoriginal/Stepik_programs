n=input()
count1=0
count2=0
for i in n:
    if i in 'ауоыиэяюёе':
        count1+=1
print('Количество гласных букв равно', count1)
for i in n:
    if i in 'бвгджзйклмнпрстфхцчшщ':
        count2+=1
print('Количество согласных букв равно', count2,)

