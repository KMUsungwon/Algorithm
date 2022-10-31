from itertools import permutations
from math import sqrt, floor
def selfNum(num):
    
    if num < 2:
        return False
    
    for i in range(2, floor(sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    
    s = set()
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            temp = ''.join(j)
            
            s.add(int(temp))
    
    for i in s:
        result = selfNum(i)
        if result:
            answer += 1
            
    return answer