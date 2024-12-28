from math import *
n=int(input())
counter=0
for i in range(1, n+1):
    counter+=1/i
s=counter-log(n)
print(s)
