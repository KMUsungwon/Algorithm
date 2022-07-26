words = input()
result = []

for i in range(1, len(words)):
    for j in range(i+1, len(words)):
        a = words[:i][::-1]
        b = words[i:j][::-1]
        c = words[j:][::-1]
        result.append(a+b+c)

print(sorted(result)[0])