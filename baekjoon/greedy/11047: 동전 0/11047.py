N, K = map(int, input().split())
count = 0
li = []
for _ in range(N):
    value = int(input())
    li.append(value)
    
li.sort(reverse=True)

while K != 0:
    if K - li[0] < 0:
        del li[0]
    else:
        K -= li[0]
        count += 1
print(count)