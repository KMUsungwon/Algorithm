from collections import deque
N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
x, y = map(int, input().split())
horse = []

def bfs(row, col):

    queue = deque()
    queue.append([row, col])

    while queue:
        dx = [-1, 1, 2, 2, 1, -1, -2, -2]
        dy = [-2, -2, -1, 1, 2, 2, 1, -1]
        
        row, col = queue.popleft()

        for i in range(8):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < N and 0 <= new_col < N:
                if graph[new_row][new_col] == 0:
                    queue.append([new_row, new_col])
                    graph[new_row][new_col] = graph[row][col] + 1

for _ in range(M):
    a, b = map(int, input().split())
    horse.append([a-1, b-1])

bfs(x-1, y-1)
for y, x in horse:
    print(graph[y][x], end=' ')