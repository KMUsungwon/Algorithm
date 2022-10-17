n = int(input())
l = []

for _ in range(n):
    a, b = map(str, input().split())
    l.append((a, int(b)))
l = sorted(l, key=lambda x: x[1])
for st in l:
    print(st[0], end=' ')