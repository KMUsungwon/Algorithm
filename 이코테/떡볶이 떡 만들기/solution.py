n, m = map(int, input().split())
li = list(map(int, input().split()))

result = 0

start = 0
end = max(li)

while start <= end:
    temp = 0
    mid = (start + end) // 2 # 높이(H)

    for i in li:
        if i > mid:
            temp += i - mid
    
    if temp < m: # 떡 길이가 부족
        end = mid - 1
    else: # 떡 길이가 부족하지 않음
        result = mid
        start = mid + 1
print(result)