from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
S = []
B = []
for _ in range(n):
    x, y = map(int, input().split())
    S.append(x)
    B.append(y)

result = float('inf')

# 1,2,3,4
for i in range(1, len(S)+1):
    temp = list(combinations(list(range(n)), i))
    
    for f in temp:
        sour = 1
        bitter = 0

        for j in range(i):
            sour *= S[f[j]]
            bitter += B[f[j]]
        
        result = min(result, abs(sour-bitter))

print(result)