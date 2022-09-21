from itertools import permutations
n, m = map(int, input().split())
l = [i for i in range(1, n+1)]
result = []
if m == 1:
    for i in permutations(l, m):
        print(i[0])
else:
    for i in permutations(l, m):
        flag = True
        for j in range(m-1):
            if i[j] > i[j+1]:
                flag = False

        if flag:
            result.append(i)

    for r in result:
        for j in range(m):
            print(r[j], end=' ')
        print()