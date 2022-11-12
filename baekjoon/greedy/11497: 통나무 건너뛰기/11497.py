from collections import deque
t = int(input())
for _ in range(t):
    result = 0
    n = int(input())
    nums = sorted(list(map(int, input().split())))

    left = []
    for i in range(0, n, 2):
        left.append(nums[i])
    
    right = deque()
    for i in range(1, n, 2):
        right.appendleft(nums[i])
    right = list(right)

    temp = left + right

    for i in range(n-1):
        result = max(result, abs(temp[i] - temp[i+1]))
    
    result = max(result, abs(temp[0] - temp[-1]))
    print(result)