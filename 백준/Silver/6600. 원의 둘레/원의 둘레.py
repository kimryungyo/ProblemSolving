from math import sqrt, pi

while True:
    try:
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        b = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        radius = (a * b * c) / sqrt((a + b + c) * (b + c - a) * (c + a - b) * (a + b - c))
        circumference = 2 * pi * radius
        print(round(circumference, 2))
    except: break