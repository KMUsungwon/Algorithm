import sys

n, l = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

for height in sorted(h):
    if l >= height:
        l += 1
print(l)