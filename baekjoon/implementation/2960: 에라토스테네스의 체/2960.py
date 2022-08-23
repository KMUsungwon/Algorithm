import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [False, False] + [True] * (n-1)
l = []
for i in range(2, n+1):
    if a[i]:
        l.append(i)
        for j in range(i*2, n+1, i):
            if a[j]:
                l.append(j)
                a[j] = False
print(l[k-1])