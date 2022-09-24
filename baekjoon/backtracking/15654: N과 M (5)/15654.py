from itertools import permutations
n, m = map(int ,input().split())
l = list(map(int, input().split()))

for i in permutations(sorted(l), m):
    for j in range(m):
        print(i[j], end=' ')
    print()