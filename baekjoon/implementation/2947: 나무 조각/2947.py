li = list(map(int, input().split()))
while li != sorted(li):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            print(' '.join(str(e) for e in li))