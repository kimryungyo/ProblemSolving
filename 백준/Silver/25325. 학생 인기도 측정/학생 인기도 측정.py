n = int(input())
students = input().split()
popularity = {student: 0 for student in students}

for _ in range(n):
    likes = input().split()
    for liked_student in likes:
        popularity[liked_student] += 1

sorted_students = sorted(popularity.items(), key=lambda x: (-x[1], x[0]))
for student, likes in sorted_students:
    print(f"{student} {likes}")