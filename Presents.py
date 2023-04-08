n = input()
array = [*map(int,input().split())]
result = []
for i,element in enumerate(array):
    print(array.index(i + 1) + 1,end= ' ')