all_number = set([i for i in range(1,10001)])
non_self_number = set()
for i in range (1, 10001):
    for j in str(i):
        i += int(j)
    non_self_number.add(i)


for i in sorted(all_number - non_self_number):
    print(i)