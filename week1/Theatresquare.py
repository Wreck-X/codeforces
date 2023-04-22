import math
array = [*map(int,input().split())]
val1 = math.ceil(array[0] / array[2])
val2 = math.ceil(array[1] / array[2])
print(val1*val2)