def get_orthogonal_value(x, y):
    if y < 0: return 4 * (y ** 2) + y + 1
    if y > 0: return 4 * (y ** 2) + 3 * y + 1
    if x < 0: return 4 * (x ** 2) - x + 1
    if x > 0: return 4 * (x ** 2) - 3 * x + 1
    return 1

def get_value(x, y):
    if abs(y) < abs(x):
        value = get_orthogonal_value(x, 0)
        if x > 0: value -= y
        else: value += y
    
    else:
        value = get_orthogonal_value(0, y)
        if y > 0: value += x
        else: value -= x
    return value

r1, c1, r2, c2 = map(int, open(0).read().split())

length = 0
rows = []
for y in range(r1, r2 + 1):
    col = []
    for x in range(c1, c2 + 1):
        value = get_value(x, y)
        if len(str(value)) > length: length = len(str(value))
        col.append(value)
    rows.append(col)

for row in rows:
    for value in row:
        print(f"{value:{length}d}", end = " ")
    print("")