result = []
while True:
    st = []
    n = list(input())
    cnt = 0

    if '-' in n:
        break

    for i in n:
        if i == "{":
            st.append(i)
        else:
            if st:
                st.pop()
            else:
                cnt += 1
                st.append('{')

    cnt += (len(st) // 2)
    result.append(cnt)

for i in range(len(result)):
    print(str(i+1) + ". " + str(result[i]))