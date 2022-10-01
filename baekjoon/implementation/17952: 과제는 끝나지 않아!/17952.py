n = int(input())
l = []
result = 0

for _ in range(n):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        l.append([temp[1], temp[2]])        
    else:
        pass

    if l:
        l[-1][1] -= 1
        if l[-1][1] == 0:
            result += l[-1][0]
            l.pop()
print(result)