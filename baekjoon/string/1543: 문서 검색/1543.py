document = input()
words = input()

answer = 0
start = 0

while start <= len(document) - len(words):
    if document[start: start+len(words)] == words:
        answer += 1
        start += len(words)
    else:
        start += 1

print(answer)