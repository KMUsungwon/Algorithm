def solution(record):
    answer = []
    users = dict()
    action = []
    
    for i in record:
        a = i.split()
        if len(a) == 3:
            if a[0] == 'Enter':
                nickname = a[2]
                users[a[1]] = nickname
            elif a[0] == 'Change':
                nickname = a[2]
                users[a[1]] = nickname
        action.append((a[0], a[1]))
    
    for act in action:
        a, b = act[0], act[1]
        if a == 'Enter':
            answer.append(users[b]+"님이 들어왔습니다.")
        elif a == 'Leave':
            answer.append(users[b]+"님이 나갔습니다.")
        
    return answer