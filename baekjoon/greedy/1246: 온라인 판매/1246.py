import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

l = sorted([int(input()) for _ in range(m)])
result = 0 # 수익
money = 0 # 얼마

for i in range(m):
    egg = min(m-i, n)

    if result <= l[i] * egg:
        result = l[i] * egg
        money = l[i]
print(money, result)
