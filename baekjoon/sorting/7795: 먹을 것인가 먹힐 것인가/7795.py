t = int(input())

for _ in range(t):
    result = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    a_index, b_index = 0, 0

    while a_index < n and b_index < m:
        if a[a_index] > b[b_index]:
            result += m - b_index
            a_index += 1
        else:
            b_index += 1

    print(result)