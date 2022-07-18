n = int(input())
m = int(input())
dis = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    dis[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][k] and dis[k][j]:
                dis[i][j] = 1

for i in range(n):
    cnt = -1 # 자기 자신 또한 카운트하기 때문에 -1 부터 시작
    for j in range(n):
        if dis[i][j] == 0 and dis[j][i] == 0:
            cnt += 1

    print(cnt)