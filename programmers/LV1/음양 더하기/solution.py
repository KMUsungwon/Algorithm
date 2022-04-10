def solution(absolutes, signs):
    for idx, sign in enumerate(signs):
        if not sign:
            absolutes[idx] = -absolutes[idx] 
    
    return sum(absolutes)