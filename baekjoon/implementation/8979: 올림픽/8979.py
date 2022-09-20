n, k = map(int, input().split())
l = []
index = 0
for _ in range(n):
    c, g, s, b = map(int, input().split())
    l.append((c, g, s, b))

l.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if l[i][0] == k:
        index = i

for i in range(n):
    if l[index][1::] == l[i][1::]:
        print(i + 1)
        break