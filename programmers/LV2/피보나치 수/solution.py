def solution(n):
    if n == 0 or n == 1:
        return n % 1234567
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b

        return a % 1234567