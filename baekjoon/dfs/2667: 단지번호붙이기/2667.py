n = int(input())

square = [list(map(int, input())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

sector = []
count = 0

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(row, col):
    global count
    visit[row][col] = True
    
    if square[row][col] == 1:
        count += 1
        
    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if new_row >=0 and new_col >=0 and new_row < n and new_col < n:
            if visit[new_row][new_col] == False and square[new_row][new_col] == 1:
                dfs(new_row, new_col)

for row in range(0, n):
    for col in range(0, n):
        if visit[row][col] == False and square[row][col] == 1:
            dfs(row, col)

            sector.append(count)
            count = 0

print(len(sector))
for i in sorted(sector):
    print(i)