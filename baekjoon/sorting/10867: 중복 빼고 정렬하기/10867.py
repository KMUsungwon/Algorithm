N = int(input())
li = list(set(map(int, input().split())))
for i in sorted(li):
    print(i, end=' ')