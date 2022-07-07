import sys, heapq
n = int(sys.stdin.readline())

h = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if not h:
            print(0)
        else:
            a = heapq.heappop(h)[1]
            print(a)

    else:
        heapq.heappush(h, [abs(x), x])