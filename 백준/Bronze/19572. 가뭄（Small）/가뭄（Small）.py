d1, d2, d3 = map(int, input().split())

a = (d1 + d2 - d3) / 2
b = (d1 + d3 - d2) / 2
c = (d2 + d3 - d1) / 2

if a > 0 and b > 0 and c > 0:
    print(1)
    print(f"{a:.1f} {b:.1f} {c:.1f}")
else: print(-1)