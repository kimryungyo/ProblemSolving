from sys import stdin
input = lambda: stdin.readline().rstrip().replace(".", "0")

moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

N = int(input())
maps = [ list(map(int, input())) for _ in range(N) ]
counts = [ [0] * N for _ in range(N) ]

for y in range(N):
    for x in range(N):
        if maps[y][x] != 0: 
            counts[y][x] = "*"
            continue

        for move in moves:
            m_y, m_x = move
            n_y, n_x = y + m_y, x + m_x

            if (0 <= n_y < N) and (0 <= n_x < N):
                counts[y][x] += maps[n_y][n_x]

                if counts[y][x] > 9:
                    counts[y][x] = "M"
                    break


for y in range(N):
    for x in range(N):
        print(counts[y][x], end = "")
    print()