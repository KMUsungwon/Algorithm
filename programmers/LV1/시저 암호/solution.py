def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = low.upper()
    answer = ''
    for i in s:
        if i in low:
            idx = low.index(i) + n
            answer += low[idx%26]
        elif i in up:
            idx = up.index(i) + n
            answer += up[idx%26]
        else:
            answer += ' '
    
    return answer