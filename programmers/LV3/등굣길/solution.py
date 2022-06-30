def solution(m, n, puddles):
    temp = [[0] * (m+1) for _ in range(n+1)]
    temp[1][1] = 1
    for row in range(1, n+1):
        for col in range(1, m+1):
            if row == 1 and col == 1:
                continue
            
            if [col, row] in puddles:
                temp[row][col] = 0
            else:
                temp[row][col] = temp[row-1][col] + temp[row][col-1]
    
    return temp[n][m] % 1000000007