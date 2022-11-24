def solution(new_id):
    new_id = new_id.lower() # 1
    alpha = ['.', '_', '-']
    
    # 2
    for i in range(len(new_id)):
        if not new_id[i].isalnum():
            if new_id[i] not in alpha:
                new_id = new_id.replace(new_id[i], 'A') # A는 제거 예정
    new_id = new_id.replace('A', '')
    
    # 3
    while True:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
        else:
            break
    
    # 4
    new_id = list(map(str, new_id))
    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id.pop()
    
    # 5
    if not new_id:
        new_id.append('a')
    
    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]
    
    if new_id[-1] == '.':
        new_id.pop()
    
    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id.append(new_id[-1])

    return ''.join(new_id)