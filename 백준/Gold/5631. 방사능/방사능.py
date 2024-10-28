from bisect import bisect_right
from sys import stdin
input = lambda: stdin.readline().rstrip()

def get_dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

testcase = 0
while True:
    N = int(input())
    if N == 0: break
    testcase += 1

    houses = [ tuple(map(int, input().split())) for _ in range(N) ]
    counts = [ 0 ] * N

    x1, y1, x2, y2, q = map(int, input().split())
    distances_1 = sorted((x1 - x) ** 2 + (y1 - y) ** 2 for x, y in houses)
    distances_2 = sorted((x2 - x) ** 2 + (y2 - y) ** 2 for x, y in houses)

    print(f"Case {testcase}:")

    for _ in range(q):
        r1, r2 = map(int, input().split())
        r1, r2 = r1 ** 2, r2 ** 2

        count_1 = bisect_right(distances_1, r1)
        count_2 = bisect_right(distances_2, r2)
        print(max(N - count_1 - count_2, 0))