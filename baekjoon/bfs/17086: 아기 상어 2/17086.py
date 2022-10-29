from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = []

queue = deque()

for i in range(n):
    temp = list(map(int, input().rstrip().split()))

    for j in range(m):
        if temp[j] == 1:
            queue.append([i, j])
    
    graph.append(temp)

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

while queue:
    row, col = queue.popleft()

    for i in range(8):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < n and 0 <= new_col < m:
            if graph[new_row][new_col] == 0:
                graph[new_row][new_col] = graph[row][col] + 1
                queue.append([new_row, new_col])

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, graph[i][j])
print(answer-1)