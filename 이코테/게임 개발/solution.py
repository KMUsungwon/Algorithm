import sys
n, m = map(int, sys.stdin.readline().split())

d = [[0]* m for _ in range(n)]

x, y, direction = map(int, sys.stdin.readline().split())
d[x][y] = 1

arr = []
for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    arr.append(li)

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 북, 서, 남, 동
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

result = 1
turn_count = 0

while True:
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_count = 0
        continue
    
    else:
        turn_count += 1
    
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(result)