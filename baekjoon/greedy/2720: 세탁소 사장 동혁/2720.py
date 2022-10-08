t = int(input())

for _ in range(t):
    result = []
    m = [25, 10, 5, 1]
    c = int(input())

    for i in m:
        cnt = c // i
        result.append(cnt)
        c = c - (i*cnt)
    
    print(*result)