from sys import stdin
input = lambda: stdin.readline().rstrip()

N = int(input())
cuboids = []

for _ in range(N):
    cuboid = list(map(int, input().split()))
    cuboids.append(cuboid)

if not cuboids: print(0)

x_min = max(cuboid[0] for cuboid in cuboids)
y_min = max(cuboid[1] for cuboid in cuboids)
z_min = max(cuboid[2] for cuboid in cuboids)
x_max = min(cuboid[3] for cuboid in cuboids)
y_max = min(cuboid[4] for cuboid in cuboids)
z_max = min(cuboid[5] for cuboid in cuboids)

if x_min < x_max and y_min < y_max and z_min < z_max:
    print((x_max - x_min) * (y_max - y_min) * (z_max - z_min))
else: print(0)