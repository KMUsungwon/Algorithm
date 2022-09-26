n = int(input())
num = list(map(int, input().split()))
result = []
for i in num:
    sum = 0
    for j in range(n):
        sum += abs(i-num[j])
    if not result:
        result.append((i, sum))
    else:
        if sum < result[0][1]:
            for k in range(len(result)):
                del result[0]
            result.append((i, sum))
        elif sum == result[0][1]:
            result.append((i, sum))

result.sort(key=lambda x:x[0])
print(result[0][0])