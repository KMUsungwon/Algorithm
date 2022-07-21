def solution(n):
    l = ['수', '박']
    answer = ''
    idx = 0
    for i in range(n):
        answer += l[idx]
        idx += 1
        if idx == 2:
            idx = 0
    return answer