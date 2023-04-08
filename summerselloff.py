n,sell= map(int,input().split())
array = []
result = 0
for i in range(n):
    subarray = [*map(int,input().split())]
    result = result + min(subarray)
    array.append(min(2*subarray[0],subarray[1]) - min(subarray[0],subarray[1])) 
array.sort()
result = result + sum(array[-sell::])
print(result)