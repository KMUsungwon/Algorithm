import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().rstrip().split()))

st = []
result = []

for i in range(n):
    while st:
        current_top_height = li[i] # 현재 탑 높이

        # 현재 탑의 높이보다 스택에 있는 탑의 높이가 낮은 경우
        if st[-1][1] < current_top_height:
            st.pop()
        # 현재 탑의 높이보다 스택에 있는 탑의 높이가 높은 경우
        else:
            result.append(st[-1][0] + 1)
            break
            
    if not st: # 스택이 비어있는 경우
        result.append(0)
    
    st.append((i, li[i])) # (인덱스, 탑의 높이) 추가
    
print(*result)