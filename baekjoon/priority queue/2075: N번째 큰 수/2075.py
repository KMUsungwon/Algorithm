import heapq
n = int(input())

h = []
for _ in range(n):
    nums = list(map(int, input().split()))

    if not h:
        for n in nums:
            heapq.heappush(h, n)
    
    else:
        for n in nums:
            if h[0] < n:
                heapq.heappush(h, n)
                heapq.heappop(h)

print(h[0])