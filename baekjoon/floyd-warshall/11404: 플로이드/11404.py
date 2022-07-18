n = int(input())
m = int(input())
INF = float('inf')

dis = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if dis[a-1][b-1] > c:
        dis[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(n):
    for j in range(n):
        if dis[i][j] == INF:
            print(0, end=' ')
        else:
            print(dis[i][j], end=' ')
    print()