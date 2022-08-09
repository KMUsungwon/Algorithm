from collections import deque
n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
tresh = []
count = 1

def bfs(x, y):
    global count
    graph[x][y] = -1

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([])
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_row = x + dy[i]
            new_col = y + dx[i]

            if 0 <= new_row < n and 0 <= new_col < m and graph[new_row][new_col] == 1:
                count += 1
                graph[new_row][new_col] = -1
                queue.append([new_row, new_col])


for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            tresh.append(count)
            count = 1
print(max(tresh))