N = int(input()) 

for _ in range(N):
    n = int(input())
    v = [0] * n      

    for i in range(n):
        nums = list(map(int, input().split()))
        k = nums[0]
        for x in nums[1:]: v[i] |= 1 << x

    mx = p = 0
    for x in range(51):
        r = 0
        for i in v:
            if not (i >> x & 1): r |= i

        r = bin(r).count('1')
        if x == 0: p = r
        elif (p ^ r) and mx < r: mx = r

    print(mx)
