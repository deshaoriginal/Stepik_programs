n=int(input())
while n>9:
    summ_digit=0
    while n>0:
        last_digit=n%10
        summ_digit+=last_digit
        n=n//10
    n=summ_digit
print(n)
print()