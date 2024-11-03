N = int(input())
DP = [ [1, 1, 1] ]
for _ in range(N - 1):
    next = [ 0 ] * 3
    next[0] += DP[-1][0] + DP[-1][1] + DP[-1][2]
    next[1] += DP[-1][0] + DP[-1][2]
    next[2] += DP[-1][0] + DP[-1][1]

    next = [ count % 9901 for count in next ]
    DP.append(next)

print(sum(DP[-1]) % 9901)