def solution(skill, skill_trees):
    answer = 0
    li = []
    for i in skill:
        li.append(i)
    
    # skill에 있는 문자 이외의 문자들 지우기
    for i in range(len(skill_trees)):
        for j in skill_trees[i]:
            if j not in li:
                skill_trees[i] = skill_trees[i].replace(j, '')
    
    # skill 순서와 일치하는지 확인
    for sk in skill_trees:
        flag = True
        for j in range(len(sk)):
            if sk[j] != skill[j]:
                flag = False
        if flag:
            answer += 1
    return answer