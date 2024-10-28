for N in map(int, open(0).read().split()):
    if N == 0: break
    count = sum((N - i) ** 2 for i in range(N))
    print(count)