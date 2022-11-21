from itertools import combinations
from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    
    for i in combinations(nums, 3):
        result = is_prime(sum(i))
        if result:
            answer += 1

    return answer