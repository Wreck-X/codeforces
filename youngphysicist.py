n = int(input())
final = []
for i in range(n):
    num = [*map(int,input().split(" "))]
    for i in num:
        final.append(i)
if sum(final) == 0:
    print("YES")
else:
    print("NO")