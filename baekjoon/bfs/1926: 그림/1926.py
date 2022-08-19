import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    global count
    visit[row][col] = True

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
                if graph[new_row][new_col] == 1 and not visit[new_row][new_col]:
                    count += 1
                    visit[new_row][new_col] = True
                    queue.append([new_row, new_col])
    

n, m = map(int, input().split())
graph = []
visit = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

pictures = []
count = 1
for row in range(n):
    for col in range(m):
        if graph[row][col] == 1 and not visit[row][col]:
            bfs(row, col)
            pictures.append(count)
            count = 1

print(len(pictures))
if not pictures:
    print(0)
else:
    print(max(pictures))