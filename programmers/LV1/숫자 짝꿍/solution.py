def solution(X, Y):
    answer = []
    for i in range(10):
        if str(i) in X and str(i) in Y:
            x_n = X.count(str(i))
            y_n = Y.count(str(i))
            
            min_n = min(x_n, y_n)
            
            for j in range(min_n):
                answer.append(i)
    
    if not answer:
        return "-1"
    elif [0] * len(answer) == answer:
        return "0"
    else:
        answer = sorted(answer, reverse=True)
        answer = list(map(str, answer))
        return ''.join(answer)