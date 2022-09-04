from itertools import combinations

while True:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    
    l = l[1::]

    for i in combinations(l, 6):
        for j in i:
            print(j, end=' ')
        print()
    print()