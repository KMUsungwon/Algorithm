import heapq, sys

def dijkstra(dis, adj, start):
    heap = []
    heapq.heappush(heap, [0, start]) # [가중치, 이동 노드]

    while heap:
        cost, node = heapq.heappop(heap)

        if dis[node] < cost:
            continue

        for c, n in adj[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost + c, n])

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

INF = float('inf')
dis = [INF] * (N+1)

adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([w, v])

start, end = map(int, sys.stdin.readline().split())
dis[start] = 0

dijkstra(dis, adj, start)

print(dis[end])