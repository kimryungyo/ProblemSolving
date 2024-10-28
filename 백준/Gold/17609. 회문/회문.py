from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    string = list(input())
    length = len(string)

    remove = -1
    for i in range(length // 2):
        if string[i] != string[-i-1]:
            remove = (i, -i-1)
            break

    if remove == -1:
        print(0)
        continue

    left, right = remove

    left_string = string.copy()
    left_string.pop(left)

    type = 1
    for i in range((length - 1) // 2):
        if left_string[i] != left_string[-i-1]:
            type = 2

    if type == 1:
        print(1)
        continue

    right_string = string.copy()
    right_string.pop(right)

    type = 1
    for i in range((length - 1) // 2):
        if right_string[i] != right_string[-i-1]:
            type = 2

    print(type)