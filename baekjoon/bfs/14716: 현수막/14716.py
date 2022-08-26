from collections import deque
M, N = map(int, input().split())
graph = []
visit = [[False] * N for _ in range(M)]
count = 0

def bfs(row, col):
    visit[row][col] = True
    dx = [0, 0, -1 ,1, 1, -1, 1, -1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    queue = deque()
    queue.append([row, col])

    while queue:
        row, col = queue.popleft()
        for i in range(8):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < M and 0 <= new_col < N:
                if graph[new_row][new_col] == 1 and not visit[new_row][new_col]:
                    visit[new_row][new_col] = True
                    queue.append([new_row, new_col])

for _ in range(M):
    graph.append(list(map(int, input().split())))

for row in range(M):
    for col in range(N):
        if graph[row][col] == 1 and not visit[row][col]:
            bfs(row, col)
            count += 1
print(count)