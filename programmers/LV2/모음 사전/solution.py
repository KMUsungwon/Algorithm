from itertools import product
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    li = []
    for r in range(1, 6):
        for i in product(vowels, repeat=r):
            w = ''.join(i)
            li.append(w)
            
    li = sorted(li)
    result = li.index(word)
    return result+1