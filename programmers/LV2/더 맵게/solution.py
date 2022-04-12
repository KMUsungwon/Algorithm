import heapq
def solution(scoville, K):
    h = []
    answer = 0
    
    for i in scoville:
        heapq.heappush(h, i)
    
    while h[0] < K:
        try:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            mix = a + (b*2)
            heapq.heappush(h, mix)
            answer += 1
        except:
            return -1
    return answer