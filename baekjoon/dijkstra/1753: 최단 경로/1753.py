import heapq

def dijkstra(dis, adj, K):
    heap = []
    heapq.heappush(heap, [0, K]) # [가중치, 이동 노드]

    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dis[n]:
                dis[n] = cost + c
                heapq.heappush(heap, [cost + c, n])

V, E = map(int, input().split())
K = int(input())

INF = float('inf')
dis = [INF for _ in range(V+1)]
dis[K] = 0 # 1->1 가중치

adj = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([w, v])

dijkstra(dis, adj, K)

for i in range(1, V+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])