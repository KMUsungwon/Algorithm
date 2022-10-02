from itertools import permutations
n = int(input())
l = list(map(int, input().split()))
result = 0
for i in permutations(l, n):
    a = 0
    for j in range(len(i)-1):
        temp = abs(i[j] - i[j+1])
        a += temp
    result = max(result, a)
print(result)