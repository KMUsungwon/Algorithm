import sys
from itertools import combinations_with_replacement
n = int (sys.stdin.readline())

roma = [1, 5, 10 ,50]
result = []
data_set = list(combinations_with_replacement(roma, n))

for d in data_set:
    result.append(sum(d))

print(len(set(result)))