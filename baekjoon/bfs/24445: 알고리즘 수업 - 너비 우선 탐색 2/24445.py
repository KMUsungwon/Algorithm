from collections import deque

def bfs(graph, start, visit):
    visit[start] = 1
    order = 2
    queue = deque([start])
    
    while queue:
        node = queue.popleft()

        for n in graph[node]:
            if not visit[n]:
                visit[n] = order
                order += 1
                queue.append(n)

n, m, r = map(int, input().split())
visit = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort(reverse=True)

bfs(graph, r, visit)
for i in range(1, n+1):
    print(visit[i])