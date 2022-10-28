import sys
input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    j, n = map(int, input().rstrip().split())
    answer = 0
    l = []
    for i in range(n):
        r, c = map(int, input().rstrip().split())
        l.append(r*c)
    
    l = sorted(l, reverse=True)

    for box in l :
        j -= box
        answer += 1
        if j <= 0:
            break
    
    print(answer)