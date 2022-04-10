def solution(numbers):
    numbers = set(numbers)
    nlist = set([i for i in range(0,10)])
    return sum(nlist-numbers)