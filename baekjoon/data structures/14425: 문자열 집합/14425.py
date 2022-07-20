n, m = map(int, input().split())
count = 0
s = []
for _ in range(n):
    s.append(input())

s = set(s)

for _ in range(m):
    word = input()
    if word in s:
        count += 1

print(count)