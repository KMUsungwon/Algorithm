n, m = map(int, input().split())
INF = float('inf')
graph = [[INF] * (n+1) for _ in range(n+1)]
result = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)
    result[a][b] = b
    result[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    result[i][j] = result[i][k]

for i in range(1, n+1):
    result[i][i] = '-'

for r in result[1::]:
    print(*r[1::])