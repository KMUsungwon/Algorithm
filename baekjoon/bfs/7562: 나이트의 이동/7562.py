from collections import deque
t = int(input())

def bfs(row, col):
    graph[row][col] = 0
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [-2, -2, -1, 1, 2, 2, 1, -1]

    queue = deque()
    queue.append([row, col])

    while queue:
        row, col = queue.popleft()

        for i in range(8):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < l and 0 <= new_col < l and graph[new_row][new_col] == -1:
                queue.append([new_row, new_col])
                graph[new_row][new_col] = graph[row][col] + 1

for _ in range(t):
    l = int(input())
    graph = [[-1] * l for _ in range(l)]

    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    bfs(r1, c1)

    print(graph[r2][c2])