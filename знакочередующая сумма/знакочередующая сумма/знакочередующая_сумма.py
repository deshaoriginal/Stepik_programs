total = 0
n=int(input())
for i in range(1, n+1):
    s=(-1)**(i+1)*i
    total += s
print(total)
