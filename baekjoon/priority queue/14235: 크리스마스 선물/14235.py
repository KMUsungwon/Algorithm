import heapq
n = int(input())
h = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(h) == 0:
            print(-1)
        else:
            gift = heapq.heappop(h)
            print(abs(gift))
    else:
        del a[0]
        for i in range(len(a)):
            heapq.heappush(h, -a[i])