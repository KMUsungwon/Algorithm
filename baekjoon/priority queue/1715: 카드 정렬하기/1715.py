import sys, heapq
h = []
n = int(sys.stdin.readline())

result = 0

for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))

while len(h) != 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)

    result += a+b
    heapq.heappush(h, a+b)

print(result)