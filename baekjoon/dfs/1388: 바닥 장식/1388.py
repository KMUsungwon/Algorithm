import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().rstrip().split())
count = 0
graph = []
for _ in range(N):
    a = input().rstrip()
    graph.append(list(a))

def w_dfs(row, col):
    graph[row][col] = None

    dx = [-1, 1]
    dy = [0, 0]

    for i in range(2):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < N and 0 <= new_col < M:
            if graph[new_row][new_col] == '-':
                w_dfs(new_row, new_col)

def h_dfs(row, col):
    graph[row][col] = None

    dx = [0, 0]
    dy = [-1, 1]

    for i in range(2):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < N and 0 <= new_col < M:
            if graph[new_row][new_col] == '|':
                h_dfs(new_row, new_col)    


for row in range(N):
    for col in range(M):
        if graph[row][col] == '-':
            w_dfs(row, col)
            count += 1
        elif graph[row][col] == '|':
            h_dfs(row, col)
            count += 1
print(count)