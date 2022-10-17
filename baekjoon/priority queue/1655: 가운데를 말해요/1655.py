# 잘못 접근한 방식 - 시간 초과
# from collections import deque
# import sys
# input = sys.stdin.readline
# n = int(input())
# queue = deque()
# for _ in range(n):
#     num = int(input())

#     if not queue:
#         queue.append(num)
#         print(num)
#     else:
#         temp = deque()
#         while queue:
#             if queue[-1] > num:
#                 a = queue.pop()
#                 temp.appendleft(a)
#             else:
#                 break
#         queue.append(num)

#         if temp:
#             for i in range(len(temp)):
#                 queue.append(temp[i])
        
#         if len(queue) % 2 == 0:
#             print(queue[len(queue)//2-1])
#         else:
#             print(queue[len(queue)//2])

import heapq, sys
input = sys.stdin.readline

n = int(input())
max_heap, min_heap = [], []

for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if len(max_heap) and len(min_heap):
        if max_heap[0] * -1 > min_heap[0]:
            a = heapq.heappop(max_heap) * -1
            b = heapq.heappop(min_heap)
        
            heapq.heappush(max_heap, b * -1)
            heapq.heappush(min_heap, a)

    print(max_heap[0] * -1)