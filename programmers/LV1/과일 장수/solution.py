def solution(k, m, score):
    answer = 0
    
    if m > len(score):
        return 0
    
    score = sorted(score)    
    count = len(score) // m
    
    while count != 0:
        temp = []
        for i in range(m):
            temp.append(score.pop())
        
        answer += min(temp) * m
        count -= 1
        
    return answer