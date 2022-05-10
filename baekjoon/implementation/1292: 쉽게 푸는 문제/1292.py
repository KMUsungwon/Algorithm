A,B = map(int, input().split())
num = 1
li = []
for i in range(1, B+1):
    for j in range(num):
        li.append(num)
    num += 1
print(sum(li[A-1:B]))