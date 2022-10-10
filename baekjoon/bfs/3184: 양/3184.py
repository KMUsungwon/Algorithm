from collections import deque
R, C = map(int, input().split())
visit = [[0] * C for _ in range(R)]

graph = []
for _ in range(R):
    graph.append(list(input()))

wolf = 0
sheep = 0

def bfs(row, col):
    visit[row][col] = 1
    o, v = 0, 0

    if graph[row][col] == 'v':
        v += 1
    elif graph[row][col] == 'o':
        o += 1
    
    queue = deque()
    queue.append([row, col])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < R and 0 <= new_col < C:
                if graph[new_row][new_col] != '#' and visit[new_row][new_col] == 0:
                    if graph[new_row][new_col] == 'v':
                        v += 1
                    elif graph[new_row][new_col] == 'o':
                        o += 1
                    elif graph[new_row][new_col] == '.':
                        pass
                    
                    queue.append([new_row, new_col])
                    visit[new_row][new_col] = 1
                
    return o, v


for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visit[i][j] == 0:
            o, v = bfs(i, j)

            if o > v:
                sheep += o
            else:
                wolf += v
print(sheep, wolf)