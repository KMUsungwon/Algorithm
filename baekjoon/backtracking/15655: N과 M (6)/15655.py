from itertools import permutations
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))

for i in permutations(l, m):
    flag = True
    for j in range(len(i)-1):
        if i[j] > i[j+1]:
            flag = False
    
    if flag:
        for k in range(len(i)):
            print(i[k], end=' ')
        print()