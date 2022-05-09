def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]
    
    for i in _reserve:
        front = i-1
        back = i+1
        if front in _lost:
            _lost.remove(front)
        elif back in _lost:
            _lost.remove(back)
        
        
    return n - len(_lost)