n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
l = sorted(l, reverse=True)
print(*l)