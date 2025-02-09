import sys
input = sys.stdin.readline

n = int(input())
ps = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    rsum = 0
    pr = ps[i - 1]
    cr = ps[i]
    arr = list(map(int, input().split()))
    for j, v in enumerate(arr, start=1):
        rsum += v
        cr[j] = pr[j] + rsum

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    tot = ps[r2][c2] - ps[r1 - 1][c2] - ps[r2][c1 - 1] + ps[r1 - 1][c1 - 1]
    inter = ps[r2 - 1][c2 - 1] - ps[r1][c2 - 1] - ps[r2 - 1][c1] + ps[r1][c1]
    print(2 * inter - tot)