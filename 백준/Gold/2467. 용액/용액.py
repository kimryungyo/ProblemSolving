n = int(input())
values = list(map(int, input().split()))

min = abs(values[0] + values[-1])
left, right = values[0], values[-1]

point1, point2 = 0, len(values) - 1

while True:
    sum = values[point1] + values[point2]
    if abs(sum) < min:
        min = abs(sum)
        left, right = values[point1], values[point2]
        if sum == 0: break

    if sum < 0: point1 += 1
    else: point2 -= 1

    if point1 == point2: break

print(left, right)