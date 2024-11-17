for line in open(0):
    M, F = map(int, line.split())
    if M == 0 and F == 0: break
    print(M + F)