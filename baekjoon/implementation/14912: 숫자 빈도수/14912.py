n, d = map(int, input().split())
li = [i for i in range(1, n+1)]
s = ""
for i in li:
    s += str(i)
a = s.count(str(d))
print(a)