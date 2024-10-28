from sys import stdin
input = lambda: stdin.readline().rstrip()

class_list = [ 0 ] * 1000001
n = int(input())

absent_students = 0

for class_num in map(int, input().split()):
    class_list[class_num] += 1

for class_num in map(int, input().split()):
    if class_list[class_num] == 0:
        absent_students += 1

    else:
        class_list[class_num] -= 1

print(absent_students)