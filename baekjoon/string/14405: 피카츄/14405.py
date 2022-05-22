S = input()
S = S.replace("pi", "*")
S = S.replace("ka", "*")
S = S.replace("chu", "*")

flag = True
for i in range(len(S)):
    if S[i] != '*':
        flag = False

if flag:
    print("YES")
else:
    print("NO")