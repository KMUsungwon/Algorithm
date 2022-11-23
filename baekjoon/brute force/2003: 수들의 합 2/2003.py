import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += nums[j]
        if temp == m:
            count += 1
        elif temp > m:
            break
print(count)