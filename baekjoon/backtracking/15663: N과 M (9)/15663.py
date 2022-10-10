import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

s = sorted(set(permutations(nums, m)))

for i in s:
    print(*list(i))