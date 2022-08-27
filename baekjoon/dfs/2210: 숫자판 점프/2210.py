import sys
sys.setrecursionlimit(100000)
def dfs(row, col, numbers):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if len(numbers) == 6:
        if numbers not in result:
            result.append(numbers)
        return

    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if 0 <= new_row < 5 and 0 <= new_col < 5:
            dfs(new_row, new_col, numbers + graph[new_row][new_col])

graph = [list(map(str, input().split())) for _ in range(5)]
result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
        
print(len(result))