from collections import deque
n = int(input())
nums = [i for i in range(1, n+1)]
queue = deque(nums)
answer =[]

while len(queue) != 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())

last = queue.pop()
answer = answer + [last] 
print(*answer)