m, n=int(input()), int(input())
if m<=n:
     for i in range(m%2-1+m, n, 2):
         print(i)
elif m>=n:
     for i in range(m%2-1+m, n-1, -2):
         print(i)
else:
    print(m)