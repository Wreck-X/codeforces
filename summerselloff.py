n,y = map(int,input().split())
dict = {}
remlist = []
subdict = {}
itemarray = []
personarray = []
for i in range(n):
    array = [*map(int,input().split())]
    itemarray.append(array[0])
    personarray.append(array[1])
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
itemarray.sort(reverse=True)
personarray.sort(reverse=True)
result = taken[-y::]
if y != 0 and result == []:
    for i in range(y):
        if itemarray[i] < personarray[i]:
            result.append(itemarray[i])
        if itemarray[i] > personarray[i]:
            pass


for i in dict:
    if dict[i][0] > dict[i][1]:
        result.append(dict[i][1])
    if dict[i][1] > dict[i][0]:
        result.append(dict[i][0])
    if dict[i][1] == dict[i][0]:
        result.append(dict[i][0])
print(sum(result))
