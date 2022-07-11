import sys
from itertools import combinations
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

result = 0
for i in combinations(li, 2):
    if i[0] + i[1] == m:
        result += 1
print(result)