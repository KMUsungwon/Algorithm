n = int(input())
nums = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-2, -1, -1):
    while nums[i] >= nums[i+1]:
        nums[i] -= 1
        cnt += 1
print(cnt)