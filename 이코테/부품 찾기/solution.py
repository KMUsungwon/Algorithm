import sys
input = sys.stdin.readline

def binary_search(target):
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == target:
            return True
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
a = list(map(int, input().rstrip().split()))
m = int(input())
b = list(map(int, input().rstrip().split()))

a.sort()

for target in b:
    result = binary_search(target)
    if not result:
        print("no", end=' ')
    else:
        print("yes", end=' ')