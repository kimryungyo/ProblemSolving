def main():
    import fractions
    import sys
    input = sys.stdin.readline
    m, i = map, int

    n, b = m(i, input().split())
    xs = ys = 0
    for _ in range(n):
        x, y = m(i, input().split())
        xs += x
        ys += y

    if xs == 0: return "EZPZ"

    answer = fractions.Fraction( -(b * n - ys), xs )
    return answer

print(main())