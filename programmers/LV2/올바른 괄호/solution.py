def solution(s):
    st = []
    for i in s:
        if  i == '(':
            st.append(i)
        elif i == ')':
            if st:
                st.pop()
            else:
                return False

    return True if not st else False