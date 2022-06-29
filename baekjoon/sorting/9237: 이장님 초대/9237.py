n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)

for i in range(n):
    li[i] += i + 1 # 일 수 추가

print(max(li) + 1)