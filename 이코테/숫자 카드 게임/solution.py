N, M = map(int, input().split())

result = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    value = min(temp)
    result = max(result, value)
print(result)