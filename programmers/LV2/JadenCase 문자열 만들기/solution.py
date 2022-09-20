def solution(s):
    l = s.split(" ")
    for i in range(len(l)):
        l[i] = l[i][:1].upper() + l[i][1:].lower()
        
    return ' '.join(l)