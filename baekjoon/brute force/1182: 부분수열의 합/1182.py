import sys
from itertools import combinations
input = sys.stdin.readline

cnt = 0
N, S = map(int, input().split())
nums = list(map(int, input().rstrip().split()))

for i in range(1, N+1):
    for j in combinations(nums, i):
        if sum(j) == S:
            cnt += 1
    
print(cnt)