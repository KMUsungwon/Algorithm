s = input()

len_s = len(s) # 문자열의 길이
temp = s.count(s[0]) # ZZZ 라면 맨 앞 문자인 Z의 개수를 구함

# 문자열의 길이가 1이거나 문자열이 한 가지의 문자로 이루어진 경우
if len_s == 1 or temp == len_s:
    print(-1)
else:
    # 문자열이 팰린드롬인 경우
    if s == s[::-1]:
        print(len_s-1)
    # 문자열이 팰린드롬이 아닌 경우
    else:
        print(len_s)