tiles = [1, 1]
for _ in range(100):
    new = tiles[-1] + tiles[-2]
    tiles.append(new)

N = int(input())
if N < 3: print(2 + N * 2)
else: print((tiles[N-1] + tiles[N-2] * 2 + tiles[N-3]) * 2)