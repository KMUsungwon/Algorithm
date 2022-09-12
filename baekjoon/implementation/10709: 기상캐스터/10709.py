H, W = map(int, input().split())
graph = [input() for _ in range(H)]
answer = [[0] * W for _ in range(H)]

cloud = False
count = 1
for i in range(H):
    for j in range(W):
        if cloud == False and graph[i][j] =='.':
            answer[i][j] = -1
        elif graph[i][j] == 'c':
            cloud = True
            count = 1
        else:
            answer[i][j] = count
            count += 1

    cloud = False
    count = 1

for i in range(H):
    for j in range(W):
        print(answer[i][j], end=' ')
    print()