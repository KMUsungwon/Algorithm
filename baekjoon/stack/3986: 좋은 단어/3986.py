n = int(input())
result = 0

for _ in range(n):
    words = input()
    s = []

    for i in range(len(words)):
        if not s:
            s.append(words[i])
        else:
            if words[i] == s[-1]:
                s.pop()
            else:
                s.append(words[i])

    if not s:
        result += 1
print(result)