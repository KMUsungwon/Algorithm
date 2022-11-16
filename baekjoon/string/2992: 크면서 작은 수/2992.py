x = int(input())

for i in range(x+1, 1000000):
    a = sorted(list(str(x)))
    b = sorted(list(str(i)))

    if a == b:
        print(i)
        break
else:
    print(0)