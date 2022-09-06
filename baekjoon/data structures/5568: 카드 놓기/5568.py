from itertools import permutations
n = int(input())
k = int(input())

l = [input().rstrip() for _ in range(n)]
result = []
for c in permutations(l, k):
    temp = ''.join(c)
    if temp not in result:
        result.append(temp)

print(len(result))