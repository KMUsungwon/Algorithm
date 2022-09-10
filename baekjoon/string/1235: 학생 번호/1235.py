n = int(input())
students = [input() for _ in range(n)]
k = -1

while True:
    l = []
    for i in range(n):
        l.append(int(students[i][k:]))
    m = list(set(l))
    
    if l == m:
        break
    else:
        k -= 1
print(abs(k))