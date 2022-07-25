n = int(input())
answer = []

for _ in range(n):
    answer.append(int(input()))

answer.sort()
for i in range(1, n+1):
    answer[i-1] = abs(answer[i-1]-i)
print(sum(answer))