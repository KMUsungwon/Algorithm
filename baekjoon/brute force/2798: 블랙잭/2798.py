from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

ans = 0
for c in combinations(num, 3):
    if ans < c[0] + c[1] + c[2] <= M:
        ans = c[0] + c[1] + c[2]
print(ans)