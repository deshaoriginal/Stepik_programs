num=int(input())
largest1 = 0
largest2 = 1
for i in range(1, num+1):
    n=int(input())
    if n>largest1:
        largest2=largest1
        largest1=n
    elif n>largest2:
            largest2=n
print(largest1)
print(largest2)

