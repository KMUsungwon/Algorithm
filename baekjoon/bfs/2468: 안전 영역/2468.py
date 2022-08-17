import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col, h):
    visit[row][col] = True
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append([row, col])

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]

            if 0 <= new_row < N and 0 <= new_col < N:
                if graph[new_row][new_col] >= h and not visit[new_row][new_col]:
                    visit[new_row][new_col] = True
                    queue.append([new_row, new_col])
                

N = int(input())

graph = []
num = set()
for _ in range(N):
    h = list(map(int, input().split()))
    graph.append(h)
    for i in h:
        num.add(i)

num = list(num)
num.sort()

answer = 1
for h in num:
    count = 0
    visit = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if graph[row][col] >= h and not visit[row][col]:
                bfs(row, col, h)
                count += 1
    
    if count > answer:
        answer = count
print(answer)        
