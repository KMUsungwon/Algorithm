n = int(input())
student = []

for _ in range(n):
    name, day, month, year = input().split()
    day, month, year = map(int, (day, month, year))
    student.append((year, month, day, name))

student.sort()
print(student[-1][3])
print(student[0][3])