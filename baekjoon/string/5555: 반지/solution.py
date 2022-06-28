string = input()
rings = int(input())

result = 0

for _ in range(rings):
    test_string = input()
    test_string += test_string

    if string in test_string:
        result += 1
    else:
        continue
        

print(result)