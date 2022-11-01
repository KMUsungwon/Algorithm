from itertools import permutations
def solution(k, dungeons):
    answer = -1
    origin_k = k
    len_d = len(dungeons)
    
    num = [i for i in range(len_d)]
    orders = []
    for i in permutations(num, len_d):
        orders.append(i)
    
    for o in orders:
        count = 0
        for j in list(o):
            if dungeons[j][0] <= k:
                k -= dungeons[j][1]
                count += 1
                
        answer = max(answer, count)
        k = origin_k
        
    return answer