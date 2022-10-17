from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    result = []
    queue = deque()

    m = int(input().rstrip())
    li = []
    if m % 10 == 0:
        for _ in range(m//10):
            li.extend(list(map(int, input().rstrip().split())))
    
    else:
        for _ in range(m//10+1):
            li.extend(list(map(int, input().rstrip().split())))

    for i in range(len(li)):
        
        if i == 0:            
            queue.append(li[i])
        else:
            temp = deque()
            while queue:
                if queue[-1] > li[i]:
                    a = queue.pop()
                    temp.appendleft(a)
                else:
                    break
            queue.append(li[i])

            if temp:
                for j in range(len(temp)):
                    queue.append(temp[j])
            
        if len(queue) % 2 == 1:
            result.append(queue[len(queue)//2])
    
    print(len(result))
    print(*result)