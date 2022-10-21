import sys
input = sys.stdin.readline
n = int(input().rstrip())

result = []
count = 1
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    result.append([s, e])

result.sort(key=lambda x: (x[1], x[0]))
k = 0
for i in range(1, n):
    if result[i][0] >= result[k][1]:
        count += 1
        k = i
print(count)