import heapq
def solution(k, score):
    answer = []
    h = []
    for i in range(len(score)):
        if i < k:
            heapq.heappush(h, score[i])
        else:
            temp = heapq.heappop(h)
            if score[i] > temp:
                heapq.heappush(h, score[i])
            else:
                heapq.heappush(h, temp)
        answer.append(min(h))
            
    return answer