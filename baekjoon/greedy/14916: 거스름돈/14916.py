import sys
input = sys.stdin.readline

n = int(input())
count = 0

while n > 0:
    if n % 5 == 0:
        m = n // 5
        count += m
        n -= 5 * m
    else:
        n -= 2
        count += 1
if n < 0:
    print(-1)
else:
    print(count)