from sys import stdin
input = stdin.readline

while True:
    p, q = map(int, input().split())
    if p == 0 and q == 0: break

    P = [input().rstrip('\n') for _ in range(p)]
    Q = [input().rstrip('\n') for _ in range(q)]

    equations = []
    rp = cp = sp = 0
    for i, line in enumerate(P):
        dot = len(line) - len(line.lstrip('.'))
        if i: equations.append((rp, cp, sp, dot))
        for ch in line[dot:]:
            if ch == '(': rp += 1
            elif ch == ')': rp -= 1
            elif ch == '{': cp += 1
            elif ch == '}': cp -= 1
            elif ch == '[': sp += 1
            elif ch == ']': sp -= 1

    cand = []
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                ok = True
                for a, b, c, d in equations:
                    if R * a + C * b + S * c != d:
                        ok = False
                        break
                if ok: cand.append((R, C, S))

    res = []
    rq = cq = sq = 0
    for line in Q:
        vals = {R * rq + C * cq + S * sq for R, C, S in cand}
        res.append(str(vals.pop() if len(vals) == 1 else -1))
        for ch in line:
            if ch == '(': rq += 1
            elif ch == ')': rq -= 1
            elif ch == '{': cq += 1
            elif ch == '}': cq -= 1
            elif ch == '[': sq += 1
            elif ch == ']': sq -= 1

    print(' '.join(res))