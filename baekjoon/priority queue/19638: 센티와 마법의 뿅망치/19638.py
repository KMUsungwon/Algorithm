import heapq
n, h, t = map(int, input().split())
height = []

giants = [int(input()) for _ in range(n)]
for g in giants:
    heapq.heappush(height, -g)

count = 0
for _ in range(t):
    max_num = -heapq.heappop(height)

    if max_num == 1:
        heapq.heappush(height, -max_num)
        break
    elif max_num < h:
        heapq.heappush(height, -max_num)
        break
    else:
        max_num //= 2
        heapq.heappush(height, -max_num)
    count += 1
    

temp = -heapq.heappop(height)

if temp < h:
    print("YES")
    print(count)
else:
    print("NO")
    print(temp)