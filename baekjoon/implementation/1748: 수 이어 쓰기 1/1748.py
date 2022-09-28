import sys
input = sys.stdin.readline
n = int(input())
result = 0

len_N = len(str(n))

for i in range(len_N -1):
    result += 9 * 10 ** i * (i+1)

print(result + (n - 10**(len_N-1) + 1) * len_N)