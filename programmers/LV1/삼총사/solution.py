from itertools import combinations
def solution(number):
    answer = 0
    l = []
    for i in combinations(number, 3):
        i = sorted(list(i))
        l.append(tuple(i))

    for i in l:
        if sum(i) == 0:
            answer += 1
    return answer