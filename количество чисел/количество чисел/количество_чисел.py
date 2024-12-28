a, b=int(input()), int(input())
counter1=0
counter2=0
for i in range(a, b+1):
    if i**3%10==4:
        counter1=counter1+1
    elif i**3%10==9:
        counter2=counter2+1
print(counter1 + counter2)

