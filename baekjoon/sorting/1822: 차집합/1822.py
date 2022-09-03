a, b = map(int, input().split())

nA = set(map(int, input().split()))
nB = set(map(int, input().split()))

res = nA - nB
res = sorted(res)
print(len(res))
if len(res):
    print(*res)