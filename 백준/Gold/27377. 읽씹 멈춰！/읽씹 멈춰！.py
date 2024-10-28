from sys import stdin
input = lambda: stdin.readline().rstrip()

tc = int(input())
for _ in range(tc):
    n = int(input())
    s, t = map(int ,input().split())
    pos, run = n, s

    while pos > 1:
        if pos % 2 == 1: 
            run += s
            pos -= 1

        else:
            dist = pos // 2
            run += min(s * dist, t)
            pos //= 2

    print(run)