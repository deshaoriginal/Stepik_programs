n=int(input())
a=1
y=0
for i in range(n):
    b=a
    a += y
    y=b
    print(b, end=' ')