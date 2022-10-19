import sys
input = sys.stdin.readline
n = int(input().rstrip())
st = []
result = []
cur = 1
flag = True
for _ in range(n):
    num = int(input())

    while cur <= num:
        st.append(cur)
        result.append('+')
        cur += 1
    
    if st[-1] == num:
        st.pop()
        result.append('-')
    
    else:
        flag = False
        print("NO")
        break

if flag:
    for r in result:
        print(r)