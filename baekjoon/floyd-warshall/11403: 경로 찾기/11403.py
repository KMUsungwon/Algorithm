n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()