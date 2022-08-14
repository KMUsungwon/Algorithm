while True:
    s = input()
    if s == '.':
        break
    
    st = []
    for i in s:
        if i == '(' or i == '[':
            st.append(i)
        
        elif i == ')':
            if st and st[-1] == '(':
                st.pop()
            else:
                st.append(i)
                break
        
        elif i == ']':
            if st and st[-1] == '[':
                st.pop()
            else:
                st.append(i)
                break
        
    if not st:
        print('yes')
    else:
        print('no')