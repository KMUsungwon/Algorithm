dic = {}
for i in range(8):
    n = int(input())
    dic[i+1] = n

a = []
b = []
sorted_by_value = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for i in range(5):
    a.append(sorted_by_value[i][0])
    b.append(sorted_by_value[i][1])
print(sum(b))
a.sort()
print(*a)