x = []
y = []
z = []

n = int(input())
for i in range(n):
    array = [*map(int,input().split())]
    z.append(array.pop())
    y.append(array.pop())
    x.append(array.pop())

if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
    print('YES')
else:
    print('NO')