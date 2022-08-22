import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    cards = deque(input().split())
    result = deque()

    first = cards.popleft()
    result.append(first)
    front = first

    while cards:
        next_card = cards.popleft()
        if next_card > front:
            result.append(next_card)
        else:
            result.appendleft(next_card)
            front = result[0]

    print(''.join(result))