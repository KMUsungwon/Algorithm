from sys import stdin
from collections import Counter
N = int(stdin.readline().rstrip())
my_card = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline().rstrip())
target_card = list(map(int, stdin.readline().split()))

counter = Counter(my_card)

for target in target_card:
    if target in counter:
        print(counter[target], end=' ')
    else:
        print(0, end=' ')