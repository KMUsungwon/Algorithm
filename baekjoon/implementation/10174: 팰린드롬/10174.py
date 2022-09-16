n = int(input())
for _ in range(n):
    pal = list(input().lower())
    print("Yes") if pal == pal[::-1] else print("No")