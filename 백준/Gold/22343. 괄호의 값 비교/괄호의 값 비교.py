from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    a = input()
    b = input()

    arr_a = [0] * 1500000
    arr_b = [0] * 1500000

    for item in range(2):
        value = 0
        for i in range(len(a)):
            if a[i] == '(': value += 1
            else:
                value -= 1
                if a[i - 1] == '(': arr_a[value] += 1

        a, b = b, a
        arr_a, arr_b = arr_b, arr_a

    for i in range(1499999):
        arr_a[i + 1] += arr_a[i] // 2
        arr_a[i] -= (arr_a[i] // 2) * 2
        arr_b[i + 1] += arr_b[i] // 2
        arr_b[i] -= (arr_b[i] // 2) * 2

    printed = False
    for i in range(1499999, -1, -1):
        if arr_a[i] < arr_b[i]:
            print("<")
            printed = True

        elif arr_a[i] > arr_b[i]:
            print(">")
            printed = True

        if printed: break

    if not printed: print("=")