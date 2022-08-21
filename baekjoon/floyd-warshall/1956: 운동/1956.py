import sys
input = sys.stdin.readline
V, E = map(int, input().split())

INF = float('inf')
dis = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    x, y, c = map(int, input().split())
    dis[x][y] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dis[i][k] + dis[k][j] < dis[i][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

result = INF
for i in range(1, V+1):
    result = min(result, dis[i][i])

if result == INF:
    print(-1)
else:
    print(result)