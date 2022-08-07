n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
count = 0

def dfs(v):
    visit[v] = 1

    for i in graph[v]:
        if not visit[i]:
            dfs(i)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visit[i]:
        if not graph[i]:
            count += 1
            visit[i] = 1
        else:
            dfs(i)
            count += 1

print(count)