import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = list(map(int, input().split()))

arr = [0]
hap = 0
for i in li:
    hap += i
    arr.append(hap)

for _ in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])