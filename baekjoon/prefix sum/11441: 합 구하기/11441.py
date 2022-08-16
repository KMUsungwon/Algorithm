import sys
input = sys.stdin.readline
N = int(input())
li = list(map(int, input().split()))
M = int(input())

arr = [0]
hap = 0
for i in li:
    hap += i
    arr.append(hap)

for _ in range(M):
    start, end = map(int, input().split())
    print(arr[end] - arr[start-1])