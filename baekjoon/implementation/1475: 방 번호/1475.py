n = input()
dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for i in str(n):
    if i in ['6', '9']:
        dic['6'] += 1
    else:
        dic[i] += 1

if dic['6'] % 2 == 0:
    dic['6'] //= 2
else:
    dic['6'] = (dic['6'] // 2) + 1

sorted_dic = sorted(dic.items(), key= lambda x: -x[1])
print(sorted_dic[0][1])