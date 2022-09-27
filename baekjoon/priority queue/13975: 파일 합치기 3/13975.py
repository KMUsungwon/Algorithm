import heapq
t = int(input())

for _ in range(t):
    k = int(input())
    num = list(map(int, input().split()))
    heapq.heapify(num)

    result = 0
    
    while num:
        a = heapq.heappop(num)
        b = heapq.heappop(num)
        result = result + (a+b)

        if not num:
            break
        
        heapq.heappush(num, a+b)
    
    print(result)