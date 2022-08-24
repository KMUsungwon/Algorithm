n = int(input())
dic = {}
for _ in range(n):
    book = input()
    if book not in dic:
        dic[book] = 1
    else:
        dic[book] += 1

dic = sorted(dic.items(), key= lambda x: x[1], reverse=True)
name = []
name.append(dic[0][0])
for i in range(1, len(dic)):
    if dic[0][1] == dic[i][1]:
        name.append(dic[i][0])
print(sorted(name)[0])