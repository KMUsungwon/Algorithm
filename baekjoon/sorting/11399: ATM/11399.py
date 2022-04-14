N = int(input())
li = list(map(int, input().split()))

li.sort()
for i in range(1, N):
    li[i] = li[i] + li[i-1]

print(sum(li))