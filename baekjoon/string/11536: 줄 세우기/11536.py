import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(sys.stdin.readline())

if l == sorted(l):
    print("INCREASING")
elif l == sorted(l, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")