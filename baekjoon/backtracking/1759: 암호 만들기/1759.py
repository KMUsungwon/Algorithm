from itertools import combinations
l, c = map(int, input().split())
a = list(map(str, input().split()))
a.sort()

result = []
vowel = ['i', 'e', 'a', 'o', 'u']
for i in combinations(a, l):
    vn, cn = 0, 0
    for j in i:
        if j in vowel:
            vn += 1
        else:
            cn += 1
    if vn >= 1 and cn >= 2:
        result.append(''.join(i))
for i in result:
    print(i)