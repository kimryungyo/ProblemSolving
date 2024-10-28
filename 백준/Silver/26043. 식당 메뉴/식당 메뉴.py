from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()


def process_meal_info(n, info_list):
    queue = deque()
    A = []
    B = []
    C = []

    for info in info_list:
        data = info.split()
        type = int(data[0])

        if type == 1:
            student_number = int(data[1])
            preferred_menu = int(data[2])
            queue.append((student_number, preferred_menu))
        
        elif type == 2:
            menu_number = int(data[1])
            student_number, preferred_menu = queue.popleft()

            if preferred_menu == menu_number:
                A.append(student_number)
            else:
                B.append(student_number)
    
    while queue:
        student_number, _ = queue.popleft()
        C.append(student_number)
    
    A.sort()
    B.sort()
    C.sort()

    print(" ".join(map(str, A)) if A else "None")
    print(" ".join(map(str, B)) if B else "None")
    print(" ".join(map(str, C)) if C else "None")

n = int(input())
info_list = [input().strip() for _ in range(n)]
process_meal_info(n, info_list)