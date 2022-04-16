T = int(input())

for _ in range(T):
    N, idx = map(int, input().split())
    li = list(map(int, input().split()))

    target = [0 for _ in range(N)]
    target[idx] = 1
    
    count = 0
    while True:
        if li[0] == max(li):
            count += 1
            if target[0] == 1:
                print(count)
                break
            else:
                li.pop(0)
                target.pop(0)
        else:
            value = li.pop(0)
            li.append(value)
            targetIdx = target.pop(0)
            target.append(targetIdx)