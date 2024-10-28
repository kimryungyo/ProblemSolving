n = int(input())
s = 0
while n > 1:
    n //= 3
    s += 1

minimum_block = [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]

def get_pixel(x, y):
    offset = [0, 0]
    for t in range(1, s + 1):

        ratio = 3 ** (s - t)
        offset_x = x // ratio
        offset_y = y // ratio

        color = minimum_block[offset_y - offset[1]][offset_x - offset[0]]
        if color == 1: return " "
        
        offset[0] = offset_x * 3
        offset[1] = offset_y * 3

    return "*"

for y in range(3**s):
    for x in range(3**s):
        print(get_pixel(x, y), end = "")
    print("")