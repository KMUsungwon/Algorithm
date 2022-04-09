N = int(input())
li = list(map(int, input().split()))
count = 0
for i in li:
    flag = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                flag = False
        
        if flag:
            count += 1
print(count)