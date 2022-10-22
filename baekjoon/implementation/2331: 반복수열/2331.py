import sys
input = sys.stdin.readline
a, p = map(int, input().rstrip().split())
l = [a]
flag = 0
while True:
    num = str(l[-1])
    s = 0
    for n in num:
        s += pow(int(n), p)
    
    if s in l:
        flag = s
        break

    l.append(s)
print(l.index(flag))