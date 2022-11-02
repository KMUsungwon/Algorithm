from collections import deque

def check(queue):
    st = []
    for i in queue:
        if i == '(' or i == '[' or i == '{':
            st.append(i)
        else:
            if not st:
                return False
            
            temp = st.pop()
            if i == ')' and temp != '(':
                return False
            elif i == '}' and temp != '{':
                return False
            elif i == ']' and temp != '[':
                return False
    
    if not st:
        return True

def solution(s):
    answer = 0
    x = len(s)
    
    queue = deque(s)
    
    for i in range(x):
        queue.rotate(-1)
        result = check(queue)
        
        if result:
            answer += 1
    return answer