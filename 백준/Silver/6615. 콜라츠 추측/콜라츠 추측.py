import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    d = {}
    x = a
    s = 0
    while True:
        d[x] = s
        if x == 1:
            break
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        s += 1
    y = b
    t = 0
    while True:
        if y in d:
            meet = y
            break
        if y == 1:
            meet = y
            break
        y = y // 2 if y % 2 == 0 else 3 * y + 1
        t += 1
    print(f"{a} needs {d[meet]} steps, {b} needs {t} steps, they meet at {meet}")