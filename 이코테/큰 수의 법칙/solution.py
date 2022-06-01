N, M, K = map(int, input().split())
li = list(map(int, input().split()))
result = 0
li.sort(reverse=True)

while True:
    for i in range(K):
        if M != 0:
            result += li[0]
            M -= 1
        else:
            break
    
    if M == 0:
        break
    result += li[1]
    M -= 1
print(result)