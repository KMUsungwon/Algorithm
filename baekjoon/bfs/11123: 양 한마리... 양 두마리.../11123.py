from collections import deque

def bfs(row, col):
    graph[row][col] = "."
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append([row, col])

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < h and 0 <= new_col < w:
                if graph[new_row][new_col] == "#":
                    graph[new_row][new_col] = "."
                    queue.append([new_row, new_col])



t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    graph = []

    for _ in range(h):
        graph.append(list(input()))
    
    count = 0
    for row in range(h):
        for col in range(w):
            if graph[row][col] == "#":
                bfs(row, col)
                count += 1
    print(count)