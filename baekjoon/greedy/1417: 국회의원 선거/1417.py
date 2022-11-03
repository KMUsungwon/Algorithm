import sys
input = sys.stdin.readline
n = int(input())
h = []

for _ in range(n):
    num = int(input())
    h.append(num)

ds = h[0]
others = h[1:]

if n == 1:
    print(0)
else:
    count = 0
    others = sorted(others, reverse=True)
    while others[0] >= ds:
        ds += 1
        others[0] -= 1
        count += 1
        others = sorted(others, reverse=True)
    print(count)