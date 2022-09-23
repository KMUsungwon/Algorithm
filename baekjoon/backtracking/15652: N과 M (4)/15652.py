from itertools import product
n, m = map(int, input().split())
l = [i for i in range(1, n+1)]

for i in product(l, repeat=m):
    flag = True
    for j in range(m-1):
        if i[j] > i[j+1]:
            flag = False
    
    if flag:
        for k in range(m):
            print(i[k], end=' ')
        print()