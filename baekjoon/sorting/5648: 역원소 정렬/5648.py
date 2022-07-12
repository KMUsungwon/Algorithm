import sys
num_list = list(map(int, sys.stdin.readline().split()))

count = num_list[0]
count -= len(num_list)-1

del num_list[0]

for i in range(len(num_list)):
    num_list[i] = int(str(num_list[i])[::-1])

while count != 0:
    input_list = list(map(int, sys.stdin.readline().split()))
    count -= len(input_list)

    for i in input_list:
        num_list.append(int(str(i)[::-1]))

for i in sorted(num_list):
    print(i)