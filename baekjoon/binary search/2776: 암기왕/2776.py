import sys
t = int(sys.stdin.readline())

def binary_search(num, note1):
    start = 0
    end = len(note1) - 1

    while start <= end:
        mid = (start + end) // 2

        if note1[mid] == num:
            return True
        elif note1[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
            
    return False

for _ in range(t):
    n = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    note1.sort()
    
    m = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))
    
    for i in note2:
        result = binary_search(i, note1)
        if result:
            print(1)
        else:
            print(0)