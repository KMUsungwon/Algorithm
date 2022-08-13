import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    global count
    graph[x][y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        new_row = x + dy[i]
        new_col = y + dx[i]

        if 0 <= new_row < M and 0 <= new_col < N and graph[new_row][new_col] == 0:
            count += 1
            dfs(new_row, new_col)

M, N, K = map(int, input().split())
count = 1

graph = [[0] * N for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = 1

sector = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            dfs(i, j)
            sector.append(count)
            count = 1
            
print(len(sector))
print(*sorted(sector))