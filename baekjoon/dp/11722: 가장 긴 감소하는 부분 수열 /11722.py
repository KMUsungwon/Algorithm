# 10 30 10 20 20 10
n = int(input())
number = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if number[j] > number[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))