l = [i for i in range(1, 21)]

for i in range(10):
    start, end = map(int, input().split())
    a = l[start-1:end][::-1]
    idx = 0
    for j in range(start-1, end):
        l[j] = a[idx]
        idx += 1
print(*l)