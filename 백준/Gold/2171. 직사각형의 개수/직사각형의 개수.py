from math import comb
from sys import stdin
input = stdin.readline

x_points = {}
y_points = {}

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    if x not in x_points: x_points[x] = set()
    x_points[x].add(y)

    if y not in y_points: y_points[y] = set()
    y_points[y].add(x)

x_list = list(x_points.keys())
x_leng = len(x_list)

count = 0
for i in range(x_leng - 1):
    x1 = x_list[i]
    for j in range(i + 1, x_leng):
        x2 = x_list[j]

        same_ys = x_points[x1] & x_points[x2]
        count += comb(len(same_ys), 2)

print(count)