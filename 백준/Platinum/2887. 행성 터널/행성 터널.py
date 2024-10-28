n, *coordinates = map(int, open(0).read().split())
x, y, z = coordinates[0::3], coordinates[1::3], coordinates[2::3]
del coordinates

x = sorted(enumerate(x), key=lambda a: a[1])
y = sorted(enumerate(y), key=lambda a: a[1])
z = sorted(enumerate(z), key=lambda a: a[1])

nodes = []
for coordinates in [x, y, z]:
    before = None
    for num, coor in coordinates:
        if before == None: before = (num, coor); continue
        nodes.append(  ( before[0], num, coor - before[1] )  )
        before = (num, coor)

nodes.sort(key=lambda a: a[2], reverse=True)

root = [None] * (n)

total_weight = 0
last_weight = None

def find_root(n):
    
    if root[n] != None: 
        root[n] = find_root(root[n])
        return root[n]
    
    return n

while nodes:
    a, b, w = nodes.pop()

    a_root, b_root = find_root(a), find_root(b)
    if a_root != b_root:
        root[b_root] = a_root

        total_weight += w
        last_weight = w

print(total_weight)