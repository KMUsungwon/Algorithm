r, c = map(int, input().split())
graph = [input() for _ in range(r)]

result = []

for i in range(r):
    temp = ""
    for j in range(c):
        if graph[i][j] != "#":
            temp += graph[i][j]
        else:
            if len(temp) >=2:
                result.append(temp)
            else:
                temp = ""

    if len(temp) >= 2:
        result.append(temp)

for i in range(c):
    temp = ""
    for j in range(r):
        if graph[j][i] != "#":
            temp += graph[j][i]
        else:
            if len(temp) >=2:
                result.append(temp)
            else:
                temp = ""

    if len(temp) >= 2:
        result.append(temp)
result.sort()
print(result[0])