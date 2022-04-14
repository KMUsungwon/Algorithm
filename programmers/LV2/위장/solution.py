def solution(clothes):
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    
    sum = 1
    for i in dic.values():
        sum *= (i+1)
    
    return sum-1 # 모두 안입은 경우 -1