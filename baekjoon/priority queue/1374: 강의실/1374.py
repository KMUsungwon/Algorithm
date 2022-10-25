import sys, heapq
input = sys.stdin.readline
n = int(input())

l = []
for _ in range(n):
    r, s, e = map(int, input().rstrip().split())
    l.append((s, e))

l.sort(key= lambda x: x[0])

h = []
heapq.heappush(h, l[0][1])

for i in range(1, n):
    if h[0] > l[i][0]:
        heapq.heappush(h, l[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, l[i][1])
print(len(h))