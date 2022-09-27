from math import factorial
n = int(input())
result = str(factorial(n))
cnt = 0
for i in range(len(result)-1, -1, -1):
    if int(result[i]) == 0:
        cnt += 1
    else:
        break
print(cnt)