n, m = map(int, input().split())

li = []
count = 0
sector = []

visit = [[False] * m for _ in range(n)]

# 상,하,좌,우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(row, col):
    global count
    visit[row][col] = True

    if li[row][col] == 0:
        count += 1
    
    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]

        if new_row < n and new_row >= 0 and new_col < m and new_col >= 0:
            if visit[new_row][new_col] == False and li[new_row][new_col] == 0:
                dfs(new_row, new_col)


for _ in range(n):
    li.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if visit[i][j] == False and li[i][j] == 0:
            dfs(i, j)
            sector.append(count)
            count = 0

print(len(sector))