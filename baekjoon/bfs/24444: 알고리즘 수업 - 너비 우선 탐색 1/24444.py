from collections import deque
n, m, r = map(int, input().split())
visit = [0] * (n+1)
graph = [[] for _ in range(n+1)]

def bfs(graph, start, visit):
    visit[start] = 1
    order = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for n in graph[node]:
            if not visit[n]:
                order += 1
                visit[n] = order
                queue.append(n)
                

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

bfs(graph, r, visit)

for i in visit[1::]:
    print(i)