a, b = map(int, input().split())

count = 1
while a != b:
    if a > b:
        count = -1
        break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        count = -1
        break
    count += 1

print(count)