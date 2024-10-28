from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
maze = [ list(input()) for _ in range(N) ]
moves = { (0, 1), (0, -1), (1, 0), (-1, 0) }

queue = deque([ (0, (0, 0)) ])
visited = { (0, 0) }

while queue:
    moved, pos = queue.popleft()
    y, x = pos

    if (y, x) == (N-1, M-1):
        print(moved + 1)
        quit()

    for move in moves:
        m_y, m_x = move
        n_y, n_x = y + m_y, x + m_x

        if (0 <= n_y < N) and (0 <= n_x < M):
            if (n_y, n_x) not in visited:
                if maze[n_y][n_x] == "1":
                    queue.append( (moved + 1, (n_y, n_x)) )
                    visited.add((n_y, n_x))