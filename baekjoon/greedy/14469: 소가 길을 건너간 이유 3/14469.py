n = int(input())
time = 0
cows = [tuple(map(int, input().split())) for _ in range(n)]
cows.sort()

for cow in cows:
    if time < cow[0]:
        time += cow[0] - time
        time += cow[1]
    else:
        time += cow[1]
print(time)