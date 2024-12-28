str = input()
count1 = 0
for i in range(len(str) - 1):
    print(str[i])
    print([i])
    if str[i + 1] == str[i]:
        count1 += 1
        print('if ', str[i + 1], end=' ')
        print([i + 1], end=' ')
        print(count1)
print()
print(count1)