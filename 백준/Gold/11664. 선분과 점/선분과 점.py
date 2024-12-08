from math import sqrt

def distance(x1, y1, z1, x2, y2, z2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

def func(t):
    Px = Ax + (Bx - Ax) * t
    Py = Ay + (By - Ay) * t
    Pz = Az + (Bz - Az) * t
    return distance(Px, Py, Pz, Cx, Cy, Cz)

left, right = 0.0, 1.0
for _ in range(100):
    m1 = (2 * left + right) / 3
    m2 = (left + 2 * right) / 3
    f1 = func(m1)
    f2 = func(m2)

    if f1 > f2: left = m1
    else: right = m2

answer = func((left + right) / 2)
print(answer)