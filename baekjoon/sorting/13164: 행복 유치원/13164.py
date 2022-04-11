N, K = map(int, input().split())
li = list(map(int, input().split()))

diff_list = []

for i in range(1, N):
    diff_list.append(li[i] - li[i-1])

diff_list.sort()

sum = 0
for i in range(N-K):
    sum += diff_list[i]
print(sum)