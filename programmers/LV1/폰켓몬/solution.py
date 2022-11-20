def solution(nums):
    answer = len(nums) // 2
    
    temp = len(set(nums))
    
    if temp < answer:
        return temp
    
    return answer