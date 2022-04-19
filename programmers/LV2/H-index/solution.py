def solution(citations):
    citations.sort() # 0, 1, 3, 5, 6
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
        
    return 0