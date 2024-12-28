num=int(input())
num2=num%10
while num>9:
    a=num%10
    num=num//10
    num2=a
print(num2)
