def solution(operations):
    answer = []
    for i in operations:
        i = i.split()
        if i[0] == 'I':
            answer.append(int(i[1]))
        elif i[0] == 'D':
            if not answer:
                continue
                
            if i[1] == '-1': # 최솟값 삭제
                temp = min(answer)
                idx = answer.index(temp)
                del answer[idx]
            elif i[1] == '1': # 최댓값 삭제
                temp = max(answer)
                idx = answer.index(temp)
                del answer[idx]
    
    if not answer:
        return [0, 0]
    answer = sorted(answer)
    return [answer[-1], answer[0]]