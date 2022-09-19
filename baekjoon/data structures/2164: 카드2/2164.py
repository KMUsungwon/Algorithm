from collections import deque
n = int(input())
li = [i for i in range(1, n+1)]
queue = deque(li)
while len(queue) != 1:
    a = queue.popleft()
    b = queue.popleft()
    queue.append(b)
print(queue[0])
