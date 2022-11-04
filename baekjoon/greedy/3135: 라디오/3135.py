import sys
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
n = int(input())

li = [abs(int(input())-b) for _ in range(n)]
print(min(abs(a-b), min(li)+1))