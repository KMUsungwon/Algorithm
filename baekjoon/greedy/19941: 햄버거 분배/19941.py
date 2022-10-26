import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
hp = list(input().rstrip())
result = 0

for i in range(n):
    if hp[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and hp[j] == 'H':
                result += 1
                hp[j] = '-'
                break
print(result)