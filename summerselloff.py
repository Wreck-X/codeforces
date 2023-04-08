n,y = map(int,input().split())

dict = {}
remlist = []
subdict = {}
for i in range(n):
    array = [*map(int,input().split())]
    dict[i] = array
    if y != 0:
        if array[0] < array[1] and array[0]*2 > array[1]:
            subdict[i] = array
            remlist.append(i)

for i in remlist:
    del dict[i]

taken = []
for i in subdict:
    taken.append(subdict[i][1])

taken.sort()
result = taken[-y::]
for i in dict:
    if dict[i][0] > dict[i][1]:
        result.append(dict[i][1])
    if dict[i][1] > dict[i][0]:
        result.append(dict[i][0])
    if dict[i][1] == dict[i][0]:
        result.append(dict[i][0])
print(sum(result))
