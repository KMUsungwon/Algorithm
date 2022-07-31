t = int(input())
times = {'300': 0, '60': 0, '10': 0}
flag = True

while t != 0:
    for time in times.items():
        if t - int(time[0]) >= 0:
            t -= int(time[0])
            times[time[0]] += 1
            break
    else:
        flag = False
        break

if flag:
    for t in times.values():
        print(t, end=' ')
else:
    print(-1)