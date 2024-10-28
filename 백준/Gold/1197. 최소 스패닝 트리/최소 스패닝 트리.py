v, e = map(int, input().split())

nodes = [ tuple(map(int, input().split())) for _ in range(e) ]
nodes.sort(key=lambda x: x[2], reverse=True)

root = { i : i for i in range(1, v + 1) }
groups = { i : {i} for i in range(1, v + 1) }

total_weight = 0

while nodes:
    a, b, w = nodes.pop()

    if root[a] != root[b]:
        a_root, b_root = root[a], root[b]

        groups[a_root] |= groups[b_root]
        for k in groups[b_root]: root[k] = root[a]

        groups[b_root] = None

        total_weight += w

print(total_weight)