def main():
    import sys
    input = sys.stdin.readline
    i, m, r = int, map, range

    N = i(input())
    ps = [ [] for _ in r(20002) ]

    for _ in r(N):
        x, y = m(i, input().split())
        ps[y].append(x)
        ps[x + 10001].append(y)

    total_leng = 0

    for points in ps:
        if points:
            points.sort()
            while points:
                end, start = points.pop(), points.pop()
                length = end - start
                total_leng += length

    print(total_leng)

main()