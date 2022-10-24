import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int ,input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
h = []
c = []

result = float('inf')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            h.append((i, j))
        elif graph[i][j] == 2:
            c.append([i, j])

for chicken in combinations(c, m):
    temp = 0
    
    for house in h:
        c_len = float('inf')
        for j in range(m):
            c_len = min(c_len, abs(house[0] - chicken[j][0]) + abs(house[1] - chicken[j][1]))
    
        temp += c_len
    result = min(result, temp)
print(result)