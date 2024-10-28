n, *perm = map(int, open(0).read().split())

for i in range(n - 1, 0, -1):
    if perm[i - 1] < perm[i]:
        for j in range(n - 1, 0, -1):
            if perm[i - 1] < perm[j]:
                perm[i - 1], perm[j] = perm[j], perm[i - 1]
                perm = perm[:i] + sorted(perm[i:])
                for num in perm: print(num, end = " ")
                exit()
                
print(-1)