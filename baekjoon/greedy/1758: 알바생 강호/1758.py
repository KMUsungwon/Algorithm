n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

s.sort(reverse=True)

rank = 1
sum = 0
for i in s:
    a = i - (rank-1)
    if a > 0:
        sum += a
    rank += 1
print(sum)