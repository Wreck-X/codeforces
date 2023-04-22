n = int(input())
for i in range(n):  
    random = input()
    list_ = [*map(int,input().split())]
    count = 0
    while len(list_ ) != len(set(list_)):
        list_.pop(0)
        count += 1
    print(count)