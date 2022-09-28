import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)

l.sort(reverse=True)

cnt = 0
for i in range(len(l)):
    a = (i+1) % 3
    if a == 0:
        continue
    cnt += l[i]
print(cnt)