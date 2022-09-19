s = input()
result = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        a = s[i:j+1]
        result.add(a)
print(len(result))