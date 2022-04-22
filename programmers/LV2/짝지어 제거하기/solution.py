def solution(s):
    li = []
    
    for i in range(len(s)):
        if not li:
            li.append(s[i])
        else:
            if s[i] == li[-1]:
                li.pop()
            else:
                li.append(s[i])
    if li:
        return 0
    else:
        return 1