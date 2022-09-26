r, c = map(int, input().split())

puzzle = [list(input()) for _ in range(r)]
        
result = []
for i in range(r):
    s = ''
    for j in range(c):
        character = puzzle[i][j]

        if character != "#":
            s += character
        else:
            if len(s) >= 2:
                result.append(s)
            s = ''

    if len(s) >= 2:
        result.append(s)

for i in range(c):
    s = ''
    for j in range(r):
        character = puzzle[j][i]

        if character != "#":
            s += character
        else:
            if len(s) >= 2:
                result.append(s)
            s = ''

    if len(s) >= 2:
        result.append(s)

print(sorted(result)[0])