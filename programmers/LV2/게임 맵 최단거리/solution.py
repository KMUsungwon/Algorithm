from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])
    queue = deque()
    queue.append([0, 0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        row, col = queue.popleft()
        
        for i in range(4):
            new_row = row + dy[i]
            new_col = col + dx[i]
            
            if 0 <= new_row < n and 0 <= new_col < m:
                if maps[new_row][new_col] == 1:
                    queue.append([new_row, new_col])
                    maps[new_row][new_col] = maps[row][col] + 1
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]