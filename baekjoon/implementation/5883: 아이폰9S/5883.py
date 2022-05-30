N = int(input())
answer = 1
li = []
for i in range(N):
    num = int(input())
    li.append(num)

for i in set(li):
    temp = li[:]
    while i in temp:
        temp.remove(i)
    
    current = temp[0]
    cnt = 1
    for j in range(1, len(temp)):
        if current == temp[j]:
            cnt += 1
        else:
            current = temp[j]
            cnt = 1
        answer = max(answer, cnt)

print(answer)