N = int(input())
li = []
count = []
for i in range(N):
    x, y = map(int, input().split())
    li.append((x, y))

for i in range(N):
    cnt = 0
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    count.append(cnt+1)

for c in count:
    print(c, end=' ')