import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
w_count = 1
b_count = 1
w_list = []
b_list = []

N, M = map(int, input().rstrip().split())
graph = []
for _ in range(M):
    wb = input().rstrip()
    graph.append(list(wb))

def w_dfs(row, col):
    global w_count
    graph[row][col] = None
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < M and 0 <= new_col < N:
            if graph[new_row][new_col] == 'W':
                w_count += 1
                w_dfs(new_row, new_col)
                

def b_dfs(row, col):
    global b_count
    graph[row][col] = None
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < M and 0 <= new_col < N:
            if graph[new_row][new_col] == 'B':
                b_count += 1
                b_dfs(new_row, new_col)

for row in range(M):
    for col in range(N):
        if graph[row][col] == 'W':
            w_dfs(row, col)
            w_list.append(w_count**2)
            w_count = 1
        elif graph[row][col] == 'B':
            b_dfs(row, col)
            b_list.append(b_count**2)
            b_count = 1
print(sum(w_list), sum(b_list))