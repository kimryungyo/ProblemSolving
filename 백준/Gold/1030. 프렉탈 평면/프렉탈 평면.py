s, n, k, r1, r2, c1, c2 = map(int, open(0).read().split())
size_in_s = (n * s, n * s)

minimum_block = [ ([0] * n) for _ in range(n) ]
margin = (n - k) // 2
for y in range(k):
    for x in range(k):
        minimum_block[margin + y][margin + x] = 1

def get_pixel(x, y):
    if n == 0: return 0

    offset = [0, 0]
    for t in range(1, s + 1):

        ratio = n ** (s - t)
        offset_x = x // ratio
        offset_y = y // ratio

        color = minimum_block[offset_y - offset[1]][offset_x - offset[0]]
        if color == 1: return 1
        
        offset[0] = offset_x * n
        offset[1] = offset_y * n

    return 0

for y in range(r1, r2 + 1):
    for x in range(c1, c2 + 1):
        print(get_pixel(x, y), end = "")
    print("")