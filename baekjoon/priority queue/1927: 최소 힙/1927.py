import heapq, sys
h = []
n = int(sys.stdin.readline())

for _ in range(n):
    x = int(int(sys.stdin.readline()))

    if x == 0:
        if not h:
            print(0)
        else:
            a = heapq.heappop(h)
            print(a)
    
    else:
        heapq.heappush(h, x)