import sys
n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    files = sys.stdin.readline().split('.')[1]
    files = files.replace('\n', '')
    if files not in dic:
        dic[files] = 1
    else:
        dic[files] += 1

result = sorted(dic.items())

for r in result:
    print(r[0], r[1])