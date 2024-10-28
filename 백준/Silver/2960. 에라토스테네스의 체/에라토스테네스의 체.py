def es(l, k):
    s = [True] * (l+1)
    s[0] = s[1] = False
    d = 0
    for n in range(2, int(1e100)):
        if s[n]:
            for m in range(n, l+1, n):
                if s[m] == True:
                    s[m] = False
                    d += 1
                    if d == k: return m

l, k = map(int, input().split())
print(es(l, k))
