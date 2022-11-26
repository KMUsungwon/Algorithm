import sys
input = sys.stdin.readline
n = int(input().rstrip())
color = input().rstrip()

temp = ''
dic = {'R':0, 'B':0}

for c in color:
    if c != temp:
        dic[c] += 1
    temp = c
print(min(dic['R'], dic['B']) + 1)