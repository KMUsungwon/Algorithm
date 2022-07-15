n = int(input())
result = n

for _ in range(n):
    words = input()

    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            continue
        elif words[i] in words[i+1:]:
            result -= 1
            break
print(result)