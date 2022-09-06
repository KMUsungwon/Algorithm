from collections import Counter
import sys
input = sys.stdin.readline
n = int(input().rstrip())
l = []
for _ in range(n):
    l.append(int(input()))

counter = Counter(l)
m = counter.most_common(n)
m.sort(key=lambda x: (-x[1], x[0]))
print(m[0][0])