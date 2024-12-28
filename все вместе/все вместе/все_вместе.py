num=int(input())
total = 0
count = 0
last=(num%10)
x=1
while num!=0:
    a=num%10
    total+=a
    count+=1
    x*=a
    mid=total/count
    first=a
    num=num//10
y=first+last
print(total)
print(count)
print(x)
print(mid)
print(first)
print(y)