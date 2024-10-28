from sys import stdin
input = lambda: stdin.readline().rstrip()

n = int(input())

buyers = []
x_coords, y_coords = [], []
for _ in range(n):
    x, y = map(int, input().split())
    buyers.append((x, y))
    x_coords.append(x)
    y_coords.append(y)

mid_x = sorted(x_coords)[n // 2]
mid_y = sorted(y_coords)[n // 2]

total_distance = 0
for x, y in buyers:
    total_distance += abs(x - mid_x) + abs(y - mid_y)

print(total_distance)