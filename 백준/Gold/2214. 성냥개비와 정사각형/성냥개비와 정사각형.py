import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    N, M = map(int, input().split())
    if N == M == 0: break

    array = [ [ 0 ] * (M * 2 + 1) for _ in range(N * 2 + 1)]
    for y in range(0, N * 2 + 1, 2):
        for x in range(0, M * 2 + 1, 2):
            array[y][x] = 1

    for y in range(N * 2 + 1):
        line = list(input())

        if y % 2 == 0:
            for i in range(len(line)):
                if line[i] == "-":
                    array[y][i * 2 + 1] = 1
        else:
            for i in range(len(line)):
                if line[i] == "|":
                    array[y][i * 2] = 1

    count = 0
    for sy in range(0, N * 2, 2):
        for sx in range(0, M * 2, 2):
            ey, ex = sy, sx

            while ((ey := ey + 2) < N * 2 + 1) and ((ex := ex + 2) < M * 2 + 1):
                is_square = True

                for x in range(sx, ex + 1):
                    if array[sy][x] == 0 or array[ey][x] == 0: 
                        is_square = False

                if not is_square: continue

                for y in range(sy, ey + 1):
                    if array[y][sx] == 0 or array[y][ex] == 0: 
                        is_square = False

                if is_square: count += 1

    print(count, "squares")