from collections import deque

N, M = map(int ,input().split())
graph = []
visit = [[0] * M for _ in range(N)]
for _ in range(N):
    temp = list(map(int, input()))
    graph.append(temp)

queue = deque()
queue.append([0, 0])
visit[0][0] = 1 # (1, 1) 좌표 방문으로 체크

while queue:
    row, col = queue.popleft()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < N and 0 <= new_col < M and visit[new_row][new_col] == 0 and graph[new_row][new_col] != 0:
            visit[new_row][new_col] = 1
            graph[new_row][new_col] = graph[row][col] + 1
            queue.append([new_row, new_col])

print(graph[N-1][M-1])