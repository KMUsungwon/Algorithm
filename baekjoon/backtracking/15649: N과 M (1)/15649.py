from itertools import permutations
n, m = map(int, input().split())
l = [i for i in range(1, n+1)]

p = permutations(l, m)
for i in p:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()