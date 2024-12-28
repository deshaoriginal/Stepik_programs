x=int(input())
count=0
for i in range(1, x+1):
    for j in range(1, i+1):
        if i%j==0:
            count+=1
    print(i, '+'*count, sep='')
    count=0
print()