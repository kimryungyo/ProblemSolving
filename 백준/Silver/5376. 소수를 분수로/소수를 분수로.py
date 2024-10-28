import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(a, b):
    while b: a, b = b, a % b
    return a

T = int(input())
for _ in range(T):
    d = input()

    if '(' in d:
        o, r = d.split('(')
        r = r[:-1]
    else:
        o, r = d, ''
    
    w, o = o.split('.')
    
    if r:
        n = int(w + o + r) - int(w + o)
        m = int('9' * len(r) + '0' * len(o))
    else:
        n = int(w + o)
        m = 10 ** len(o)
    
    g = gcd(n, m)
    print(f"{n // g}/{m // g}")