from collections import deque
n, m = map(int, input().split())
graph = []
s, w = 0, 0
for _ in range(n):
    graph.append(list(input()))

visit = [[0] * m for _ in range(n)]

def bfs(row, col):
    visit[row][col] = 1
    sheep, wolf = 0, 0

    if graph[row][col] == 'v':
        wolf += 1
    elif graph[row][col] == 'k':
        sheep += 1

    queue = deque()
    queue.append([row, col])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < n and 0 <= new_col < m:
                if graph[new_row][new_col] != '#' and visit[new_row][new_col] == 0:
                    visit[new_row][new_col] = 1
                    queue.append([new_row, new_col])

                    if graph[new_row][new_col] == 'k':
                        sheep += 1
                    elif graph[new_row][new_col] == 'v':
                        wolf += 1
    

    return sheep, wolf


for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and visit[i][j] == 0:
            sheep, wolf = bfs(i, j)

            if sheep > wolf:
                s += sheep
            else:
                w += wolf
print(s, w)
