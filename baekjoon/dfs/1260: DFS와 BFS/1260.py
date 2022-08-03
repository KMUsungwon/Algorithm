from collections import deque
def DFS(start):
    visit[start] = 1
    print(start, end=' ')

    for i in graph[start]:
        if not visit[i]:
            DFS(i)

def BFS(start):
    visit[start] = 1
    queue = deque([start])

    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not visit[i]:
                queue.append(i)
                visit[i] = 1
    

n, m, v = map(int, input().split())

visit = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

DFS(v)
visit = [0] * (n+1)
print()
BFS(v)