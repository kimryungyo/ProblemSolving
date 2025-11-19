from collections import deque
N, M = map(int, input().split())

base_coins = []
table = [ ["."] * M for _ in range(N) ]

for i in range(N):
    line = input()
    for j in range(M):
        block = line[j]
        if block == "o":
            base_coins.append( (i, j) )
        elif block == "#":
            table[i][j] = "#"

def simulate(coin, to):
    i, j = coin
    if to == "L":
        y, x = (i, j-1)
    elif to == "R":
        y, x = (i, j+1)
    elif to == "U":
        y, x = (i-1, j)
    elif to == "D":
        y, x = (i+1, j)
    
    drop = 0
    if y < 0 or y > N-1 or x < 0 or x > M-1:
        drop = 1
        return (y, x, drop)

    if table[y][x] == "#":
        return (i, j, drop)

    return (y, x, drop)

visited = set()
queue = deque( [ (0, tuple(base_coins)) ] )
while queue:
    count, coins = queue.popleft()
    visited.add(tuple(sorted(coins)))

    if count >= 10:
        print(-1)
        quit()
    
    for to in "LRUD":
        drops = 0
        ncoins = []
        for coin in coins:
            ny, nx, drop = simulate(coin, to)
            drops += drop
            ncoins.append( (ny, nx) )

        ncoins = tuple(sorted(ncoins))
        if drops == 2:
            continue
        elif drops == 1:
            print(count+1)
            quit()
        elif ncoins not in visited:
            queue.append( (count+1, ncoins) )

print(-1)