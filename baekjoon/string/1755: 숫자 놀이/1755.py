M, N = map(int, input().split())
li = []
dic = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero"}

for i in range(M, N+1):
    st = ''.join(dic[j] for j in str(i))
    # print(st)
    li.append((i, st))

li.sort(key= lambda x: x[-1])

flag = 0
for i in range(len(li)):
    print(li[i][0], end=' ')
    flag += 1

    if flag == 10:
        flag = 0
        print()