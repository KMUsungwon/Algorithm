import sys, heapq
input = sys.stdin.readline
n = int(input().rstrip())
result = 0
course = []
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    course.append((s, e))

course = sorted(course, key= lambda x: x[0])
h = []

# 제일 시작 시간이 빠른 회의의 끝나는 시간
heapq.heappush(h, course[0][1])

for i in range(1, n):
    if h[0] > course[i][0]: # 다음 회의를 이어서 할 수 없는 경우
        heapq.heappush(h, course[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, course[i][1])
print(len(h))