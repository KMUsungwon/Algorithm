N = int(input())
my_card = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

l = []
my_card.sort()

def binary_search(my_card, target):
    start = 0
    end = len(my_card) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == my_card[mid]:
            return 1
        elif my_card[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in cards:
    result = binary_search(my_card, i)
    l.append(result)

print(' '.join(map(str, l)))