def main():
    r, c = map(int, input().split())
    h = []
    for i in range(r):
        h.append([])
        h[i] = [int(h) for h in input().split()]

    tsa = r * c * 2

    for x in range(r):
        for y in range(c):
            tsa += h[x][y] * 4

            if x > 0:
                if h[x][y] < h[x - 1][y]: tsa -= h[x][y]
                else: tsa -= h[x - 1][y]
            if x < r - 1:
                if h[x][y] < h[x + 1][y]: tsa -= h[x][y]
                else: tsa -= h[x + 1][y]
            
            if y > 0:
                if h[x][y] < h[x][y - 1]: tsa -= h[x][y]
                else: tsa -= h[x][y - 1]
            if y < c - 1:
                if h[x][y] < h[x][y + 1]: tsa -= h[x][y]
                else: tsa -= h[x][y + 1]

    print(tsa)

main()

