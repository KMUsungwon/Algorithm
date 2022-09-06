import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
for _ in range(M):
    a = list(input().rstrip())
    b = list(map(int, a))
    graph.append(b)

temp = graph[-1].copy()

def bfs(row, col):
    graph[row][col] = -1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append([row, col])
    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < M and 0 <= new_col < N:
                if graph[new_row][new_col] == 0:
                    queue.append([new_row, new_col])
                    graph[new_row][new_col] = -1

for row in range(1):
    for col in range(N):
        if graph[row][col] == 0:
            bfs(row, col)

print("YES") if temp != graph[-1] else print("NO")