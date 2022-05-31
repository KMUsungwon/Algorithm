N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == target:
            return True
        
        elif a[mid] > target:
            end = mid - 1
        elif a[mid] < target:
            start = mid + 1
    
    return False

for i in range(M):
    flag = binary_search(b[i])

    if flag:
        print(1)
    else:
        print(0)