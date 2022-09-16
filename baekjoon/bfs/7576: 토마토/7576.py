from collections import deque
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
queue = deque()

def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < N and 0 <= new_col < M:
                if graph[new_row][new_col] == 0:
                    graph[new_row][new_col] = graph[row][col] + 1
                    queue.append([new_row, new_col])
        
        

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

bfs()
flag = True
for i in graph:
    for j in i:
        if j == 0:
            flag = False
    
    result = max(result, max(i))

if not flag:
    print(-1)
else:
    print(result-1)