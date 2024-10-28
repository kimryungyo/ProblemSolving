n = int(input())
buckets = []

points = []
for _ in range(n):
    b, h, w, d = map(int, input().split())

    points.append( (b, "start", w * d ) )
    points.append( (b + h, "end", w * d ) )

points.sort(key=lambda x: x[0])
waters = int(input())

active = 0
volume = 0
height = 0

for point in points:

    bf_height = height
    height = point[0] - height

    add = active * height
    if volume + add < waters: volume += add
    else:
        remain = (waters - volume) / active
        print(bf_height + remain)
        quit()
    
    if point[1] == "start":
        active += point[2]

    elif point[1] == "end":
        active -= point[2]
        
    height = point[0]
    
print("OVERFLOW")