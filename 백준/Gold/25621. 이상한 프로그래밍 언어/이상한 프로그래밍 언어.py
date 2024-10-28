from sys import stdin
input = lambda: stdin.readline().rstrip()

mod = 10 ** 9 + 7

def exp(c, k):
    e, x = c[0], int(c[1:])
    d, m = k
    if e == "+": m += x
    elif e == "-": m -= x
    else:
        d *= x
        m *= x

    return [ d, m ]

n, s = map(int, input().split())
k = [ 0, s ]

for _ in range(n):
    c1, c2 = input().split()

    rs = [ exp(c1, k), exp(c2, k) ]
    for i in range(len(rs)):
        d, m = rs[i]

        if m < 0:
            if d < 1:
                rs[i] = [ 0, 0 ]
                continue
            else:
                d -= 1
                m += mod

        new_d = d + (m // mod)
        new_m = m % mod

        rs[i] = [ new_d, new_m ]

    k = max(rs)
    if k[0] > 1e100: k[0] = 10 ** 100

print(k[1])