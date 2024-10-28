from collections import deque
from sys import stdin
input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):

    M, N, K = map(int, input().split())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cabbages = set()
    for _ in range(K):
        postion = tuple(map(int, input().split()))
        cabbages.add(postion)

    worms = 0
    while cabbages:
        worms += 1
        union = cabbages.pop()
        queue = deque([ union ])

        while queue:
            field = queue.popleft()
            x, y = field

            for i in range(4):
                n_x, n_y = x + dx[i], y + dy[i]
                if (n_x, n_y) in cabbages:
                    queue.append( (n_x, n_y) )
                    cabbages.remove( (n_x, n_y) )

    print(worms)