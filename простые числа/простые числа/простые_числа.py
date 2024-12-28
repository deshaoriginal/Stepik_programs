a, b=int(input()), int(input())
for i in range(a, b+1):
    digit=1
    for j in range(2, i+1):
        if i%j==0:
            digit+=1
    if digit==2:
         print(i)