N = int(input())
graph = [list(input()) for _ in range(N)]
v = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] =="Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                v[i][j] = 1

result = 0
for i in v:
    result = max(result, sum(i))
print(result)