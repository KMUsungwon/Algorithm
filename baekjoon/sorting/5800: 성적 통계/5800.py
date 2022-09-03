k = int(input())
for i in range(k):
    students = list(map(int, input().split()))
    students = students[1::]
    a = max(students)
    b = min(students)

    students.sort(reverse=True)
    gap = 0
    for j in range(len(students)-1):
        if gap < students[j] - students[j+1]:
            gap = students[j] - students[j+1]
    
    print("Class {0}".format(i+1))
    print("Max {0}, Min {1}, Largest gap {2}".format(a, b, gap))
