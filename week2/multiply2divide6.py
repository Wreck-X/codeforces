n = int(input())
for i in range(n):
    num = int(input())
    count2 = 0
    count3 = 0
    while num % 2 == 0:
        num = num // 2
        count2+= 1
    while num % 3 == 0:
        num = num // 3
        count3 += 1
    if count2 > count3:
        print(-1)
        continue
    if num == 1:
        print((count3 - count2) + count3)
    else:
        print(-1)