L = float(input())
red = sorted(list(map(float, input().split())))
blue = sorted(list(map(float, input().split())))
yellow = sorted(list(map(float, input().split())))

points = {
    "red": red,
    "blue": blue,
    "yellow": yellow
}
current_length = L

for color in ["red", "blue", "yellow"]:
    p, q = points[color]
    if p == q:
        continue

    crease = (p + q) / 2

    if crease <= current_length - crease:
        new_length = current_length - crease
        for key in points:
            new_coords = []
            for x in points[key]:
                if x >= crease:
                    new_coords.append(x - crease)
                else:
                    new_coords.append(crease - x)
            points[key] = new_coords
    else:
        new_length = crease
        for key in points:
            new_coords = []
            for x in points[key]:
                if x <= crease:
                    new_coords.append(x)
                else:
                    new_coords.append(2 * crease - x)
            points[key] = new_coords

    current_length = new_length

print(f"{current_length:.1f}")
