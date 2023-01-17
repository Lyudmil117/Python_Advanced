student_grades = {}
n = int(input())

for _ in range(n):
    data = input().split(" ")
    student = data[0]
    mark = float(data[1])

    if student not in student_grades:
        student_grades[student] = []

    student_grades[student].append(mark)

for student, grade in student_grades.items():
    print(f"{student} -> {' '.join([str(f'{mark:.2f}') for mark in grade])} (avg: {(sum(grade) / len(grade)):.2f})")