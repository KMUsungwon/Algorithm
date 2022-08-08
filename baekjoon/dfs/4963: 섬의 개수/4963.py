import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 상하좌우 대각선
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    graph[x][y] = 0

    for i in range(8):
        new_x = x + dx[i] 
        new_y = y + dy[i]

        if new_x >=0 and new_x < h and new_y >= 0 and new_y < w:
            if graph[new_x][new_y] == 1:
                dfs(new_x, new_y)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    count = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                dfs(x, y)
                count += 1

    print(count)