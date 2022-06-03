N = int(input())
li = input().split()

x, y = 1, 1

LRUD = ['L', 'R', 'U', 'D']

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for l in li:
    for i in range(len(LRUD)):
        if l == LRUD[i]:
            new_x = x + dx[i]
            new_y = y + dy[i]
    
    if new_x < 1 or new_y < 1 or new_x > N or new_y > N:
        continue
    
    x, y = new_x, new_y

print(x, y)