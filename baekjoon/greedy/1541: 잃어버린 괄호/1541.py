n = input().split('-')
result = 0

for i in n[0].split('+'):
    result += int(i)

for i in range(1, len(n)):
    a = n[i].split('+')
    for j in a:
        result -= int(j)

print(result)