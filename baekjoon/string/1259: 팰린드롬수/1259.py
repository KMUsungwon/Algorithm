while True:
    num = int(input())
    if num == 0:
        break
    print("yes") if num == int(str(num)[::-1]) else print("no")