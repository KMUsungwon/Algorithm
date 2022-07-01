pos = input()

row = int(pos[1])

# 문자 'a,b,c..'를 숫자로 변경하기
col = int(ord(pos[0])) - int(ord('a')) + 1

count = 0

# 나이트 이동 범위
nights = [(-2, 1), (-2, -1), (2, 1), (2, -1),
(1, -2), (-1, -2), (1, 2), (-1, 2)]

for n in nights:
    new_row = row + n[0]
    new_col = col + n[1]

    if new_row >=1 and new_row <=8 and new_col >=1 and new_col <= 8:
        count += 1

print(count)