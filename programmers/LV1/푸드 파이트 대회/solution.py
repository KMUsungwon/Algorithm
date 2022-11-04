from collections import deque
def solution(food):
    answer = ''
    left = deque()
    right = deque()
    
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        
        for j in range(food[i]//2):
            left.append(i)
            right.appendleft(i)
    
    left = list(left)
    right = list(right)
    answer = left + [0] + right
    answer = list(map(str, answer))
    
    return ''.join(answer)