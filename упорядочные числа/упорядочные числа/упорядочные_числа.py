n = int(input())
flag = True
while n//10 > 0:  
    last_d1 = n % 10 
    n = n // 10  
    last_d2 = n % 10  
    if last_d2 < last_d1:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO') 
    

