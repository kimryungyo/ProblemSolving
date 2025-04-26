N = int(input())
if N == 1: print(1)
else:
    res = []
    if N % 2:
        m = N // 2
        for i in range(1, m + 1):
            res.append(i)
            res.append(N - i)
        res.append(N)
    else:
        m = N // 2
        for i in range(1, m):
            res.append(i)
            res.append(N - i)
        res.append(N)
        res.append(m)
    print(*res)