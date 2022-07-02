from math import factorial
t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # mCn

    result = factorial(m) // (factorial(m-n) * factorial(n))
    print(result)