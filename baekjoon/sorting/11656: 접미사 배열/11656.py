words = input()

l = []
for i in range(len(words)):
    l.append(''.join(words[i:]))

for word in sorted(l):
    print(word)