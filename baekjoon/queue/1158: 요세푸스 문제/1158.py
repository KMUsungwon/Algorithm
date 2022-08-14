N, K = map(int, input().split())
result = []
li = [i for i in range(1, N+1)]

n = 0
for i in range(N):
    n += (K-1)
    if n >= len(li):
        n %= len(li)
    
    result.append(str(li[n]))
    li.pop(n)
print('<' + ', '.join(result) + '>')