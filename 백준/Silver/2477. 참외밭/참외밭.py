from sys import stdin
input = lambda: stdin.readline().rstrip()

lengs = [(0, 0) for _ in range(12)]

k = int(input())

for i in range(6):
    direction, length = map(int, input().split())
    lengs[i] = lengs[i + 6] = (direction, length)

for i in range(3, 12):
    if lengs[i][0] == lengs[i - 2][0] and lengs[i - 1][0] == lengs[i - 3][0]:
        big = lengs[i + 1][1] * lengs[i + 2][1]
        small = lengs[i - 1][1] * lengs[i - 2][1]
        break

print(k * (big - small))