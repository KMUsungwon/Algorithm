import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    doc = deque(list(map(int, input().split())))
    count = 0

    while doc:
        max_num = max(doc)
        a = doc.popleft()
        m -= 1

        if a == max_num:
            count += 1
            if m < 0:
                print(count)
                break
        
        else:
            doc.append(a)
            if m < 0:
                m = len(doc) - 1