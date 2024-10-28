from sys import stdin
input = lambda: map(int, stdin.readline().split())

cars = [ 0 ] * 100
a, b, c = input()
b *= 2
c *= 3

for _ in range(3):
    for t in range(*input()): cars[t] += 1

cost = 0
for car in cars:
    if car: cost += a if car == 1 else (b if car == 2 else c)

print(cost)