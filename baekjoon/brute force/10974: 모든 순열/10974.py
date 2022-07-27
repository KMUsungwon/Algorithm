from itertools import permutations
n = int(input())
l = [i for i in range(1, n+1)]

result = permutations(l, n)
for p in result:
    for i in range(len(p)):
        print(p[i], end=' ')
    print()