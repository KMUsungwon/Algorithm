def solution(s):
    answer = []
    li = s.split(' ')
    
    for word in li:
        temp = ''
        for i in range(0, len(word)):
            if i%2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
    return " ".join(answer)