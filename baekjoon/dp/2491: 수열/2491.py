n = int(input())
nums = [0] + list(map(int, input().split()))

dp1 = [0] * (n+1)
dp2 = [0] * (n+1)

# 앞에서부터
dp1[1] = 1
for i in range(2, n):
    if nums[i-1] <= nums[i]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    else:
        dp1[i] = 1

# 뒤에서부터
dp2[-1] = 1
for i in range(n-1, 0, -1):
    if nums[i] >= nums[i+1]:
        dp2[i] = max(dp2[i], dp2[i+1]+1)
    else:
        dp2[i] = 1

print(max(max(dp1), max(dp2)))