def find(x, parent):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, size):
    a = find(a, parent)
    b = find(b, parent)
    if a == b:
        return False
    if a < b:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

def f(n):
    return n * (n - 1) // 2

def g(n):
    return n * (n - 1) * (n + 1) // 6

num_nodes = int(input())
parent = [i for i in range(num_nodes + 1)]
size = [1] * (num_nodes + 1)

total_f1, total_f2 = 0, 0
for i in range(num_nodes - 1):
    node = int(input())
    a = find(node, parent)
    b = find(node + 1, parent)
    if a != b:
        total_f1 -= f(size[a]) + f(size[b])
        total_f2 -= g(size[a]) + g(size[b])
        union(a, b, parent, size)
        a = find(a, parent)
        total_f1 += f(size[a])
        total_f2 += g(size[a])
    print(total_f1, total_f2)