import sys
sys.setrecursionlimit(10000)
T = int(input())

def dfs(row, col):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if (0 <= new_row < N) and (0 <= new_col < M):
            if graph[new_row][new_col] == 1:
                graph[new_row][new_col] = -1
                dfs(new_row, new_col)

for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    
    for i in range(K):
        col, row = map(int, input().split())
        graph[row][col] = 1
    
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1:
                dfs(row, col)
                count += 1
    
    print(count)