def one_count(n):
    answer = 0
    while n>0:
        if n%2==1:
            answer +=1
        n //= 2
    return answer

def solution(n):
    
    oneCnt = one_count(n)
    
    while True:
        n += 1
        nextOneCnt = one_count(n)
        if oneCnt == nextOneCnt:
            break
    return n