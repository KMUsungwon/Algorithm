n = int(input())

triangles = []
for i in range(n):
    num = list(map(int, input().split()))
    triangles.append(num)

for i in range(1, n):
    for j in range(len(triangles[i])):
        if j == 0:
            triangles[i][j] += triangles[i-1][j]
        elif j == i:
            triangles[i][j] += triangles[i-1][j-1]
        else:
            triangles[i][j] += max(triangles[i-1][j], triangles[i-1][j-1])

print(max(triangles[-1]))