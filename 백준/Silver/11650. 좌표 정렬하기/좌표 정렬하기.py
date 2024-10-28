n = int(input())

coordinates = []

for _ in range(n):

    x, y = map(int, input().split())

    coordinates.append(  (x, y, x*1e10 + y)  )

coordinates.sort(key=lambda a: a[2])

for coordinate in coordinates:

    print(coordinate[0], coordinate[1])