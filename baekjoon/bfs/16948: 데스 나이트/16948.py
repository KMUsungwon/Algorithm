from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n and graph[new_x][new_y] == -1:
                graph[new_x][new_y] = graph[x][y] + 1
                queue.append([new_x, new_y])

n = int(input())
graph = [[-1] * n for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
r1, c1, r2, c2 = map(int, input().split())

bfs(r1, c1)
print(graph[r2][c2])