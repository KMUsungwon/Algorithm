n = int(input())
nums = list(map(int ,input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
temp = []
flag = max(dp)

for i in range(n-1, -1, -1):
    if dp[i] == flag:
        temp.append(nums[i])
        flag -= 1
temp = temp[::-1]
print(*temp)