import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
box = list(map(int, input().rstrip().split()))
child = list(map(int, input().rstrip().split()))

box_h = []

for b in box:
    heapq.heappush(box_h, -b)

for c in child:
    a = -heapq.heappop(box_h)

    if a > c:
        heapq.heappush(box_h, -(a-c))
    
    elif a < c:
        print(0)
        exit(0)

print(1)