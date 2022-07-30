N, M = map(int, input().split())

d = set([input() for _ in range(N)])
b = set([input() for _ in range(M)])

count = 0
db = []

for i in d:
    if i in b:
        count += 1
        db.append(i)
db.sort()
print(count)
for i in db:
    print(i)