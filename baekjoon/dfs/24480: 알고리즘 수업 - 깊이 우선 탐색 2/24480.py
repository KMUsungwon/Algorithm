import sys
sys.setrecursionlimit(100000)
n, m, r = map(int, input().split())
visit = [0] * (n+1)
graph = [[] for _ in range(n+1)]
order = 1

def dfs(graph, node, visit):
    global order

    for n in graph[node]:
        if not visit[n]:
            order += 1
            visit[n] = order
            dfs(graph, n, visit)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort(reverse=True)

visit[r] = 1
dfs(graph, r, visit)

for i in visit[1::]:
    print(i)