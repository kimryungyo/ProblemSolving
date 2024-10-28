from sys import stdin, setrecursionlimit
setrecursionlimit(25600)
input = lambda: stdin.readline().rstrip()

table = 100005

def find(node, p, dist):
    if p[node] == -1:
        return node
    
    parent = find(p[node], p, dist)
    dist[node] += dist[p[node]]
    p[node] = parent
    return parent

def merge(a, b, w, p, dist):
    root_a = find(a, p, dist)
    root_b = find(b, p, dist)
    
    if root_a == root_b:
        return
    
    dist[root_b] = dist[a] - dist[b] + w
    p[root_b] = root_a

while True:
    p = [-1] * table
    dist = [0] * table
    n, m = map(int, input().split())

    if n == 0 and m == 0:  break
    
    for _ in range(m):
        line = input().split()
        op = line[0]
        a, b = map(int, line[1:3])
        
        if op == '!':
            w = int(line[3])
            merge(a, b, w, p, dist)
        else:
            if find(a, p, dist) != find(b, p, dist): print("UNKNOWN")
            else: print(dist[b] - dist[a])