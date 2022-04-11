def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    count = 0
    for l in lottos:
        if l in win_nums:
            count += 1

    high_rank = count+lottos.count(0)
    row_rank = count
    
    
    return [rank[high_rank], rank[row_rank]]