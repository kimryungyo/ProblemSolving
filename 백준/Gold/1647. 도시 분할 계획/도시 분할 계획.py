from sys import stdin
input = lambda: stdin.readline().rstrip()

v, e = map(int, input().split())

nodes = [ tuple(map(int, input().split())) for _ in range(e) ]
nodes.sort(key=lambda x: x[2], reverse=True)

root = [None] * (v + 1)

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

print(total_weight - last_weight)